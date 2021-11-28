#Author: Kridtity Ikhlaas Lawang
#Program Name: BlackHat IT Payroll System

#License: GNU GPLv3.0
#Status: Release
#Version: 1.0
#Release Date: 29-11-2021
#Description: Payroll calculation system for Blackhat IT

#Copyright (C) 2021 Kridtity Lawang

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#Import modules (paymod is self-created)
import paymod
import re
import webbrowser
import importlib
import payroll

#Initialise lists
first_names_list = []
last_names_list = []
positions_list = []
hours_list = []
overtime_hours_list = []
holiday_hours_list = []
salaries_list = []
gross_incomes_list = []
net_incomes_list = []
taxes_list = []
supers_list = []

#Function to prevent program from closing immediately after finishing running the code sequence by waiting for random input (i.e. wait until key pressed to close program)
def wait_to_close():
    i = input("")
    quit()

#Print intro and main menu choices
print("------------------------------\n"
      "| BlackHat IT Payroll System |\n"
      "------------------------------\n")

menu_select = input("------------------------------\n"
                    "|         Main  Menu         |\n"
                    "------------------------------\n"
                    "Enter: I => Input employee pay details\n"
                    "       P => Print last payroll session in IDLE Shell/command line\n"
                    "       H => Help manual\n"
                    "       S => Change settings\n"
                    "       E => Exit the program\n").upper()

if menu_select == "I":
    #Print mode choices: hourly rate for hours worked in pay cycle or pay cycle amounts from annual salary
    mode = input("------------------------------\n"
                 "| Input employee pay details |\n"
                 "------------------------------\n"
                 "Enter: H => Calculate payroll based on hourly rate\n"
                 "            and hours worked\n"
                 "       S => Calculate payroll based on annual salary\n").upper()

    if mode == "H":
        #Pay cyle to be used
        paycycle = int(input("Enter pay cycle in full weeks: "))

        #Get number of employees for iteration
        num_employees = int(input("Enter number of employees: "))
        print("")

        #Get employee details, calculate payment values, and append to list
        for x in range(num_employees):
            #Get employee details
            print("Employee {}:".format(x + 1))
            last_name = input("Last name: ").upper()
            first_name = input("First name: ").capitalize()
            position = input("Position: ").title()
            print("")

            #Get employee work details for pay cycle
            hours_worked = float(input("Standard hours worked in pay cycle: "))
            overtime_hours_worked = float(input("Overtime hours worked in pay cycle: "))
            holiday_hours_worked = float(input("Holiday hours worked in pay cycle: "))
            print("\n"
                  "------------------------------\n")

            #Calculate payment values
            #Note: calculate_from_wage function tuple value order is wage, superannuation, paycycle_tax, net_wage
            payment_values = paymod.calculate_from_wage(position, paycycle, hours_worked, overtime_hours_worked, holiday_hours_worked)            
            
            #Append values to lists
            first_names_list.append(first_name)
            last_names_list.append(last_name)
            positions_list.append(position)
            hours_list.append(hours_worked)
            overtime_hours_list.append(overtime_hours_worked)
            holiday_hours_list.append(holiday_hours_worked)
            salaries_list.append(paymod.employee_pay_details(position)[0])
            gross_incomes_list.append(payment_values[0])
            net_incomes_list.append(payment_values[3])
            taxes_list.append(payment_values[2])
            supers_list.append(payment_values[1])
        
                  
    elif mode == "S":
        #Pay cyle to be used
        paycycle = int(input("Enter pay cycle in full weeks: "))

        #Get number of employees for iteration
        num_employees = int(input("Enter number of employees: "))
        print("")

        #Get employee details, calculate payment values, and append to list
        for x in range(num_employees):
            #Get employee details
            print("Employee {}:".format(x + 1))
            last_name = input("Last name: ").upper()
            first_name = input("First name: ").capitalize()
            position = input("Position: ").title()
            print("\n"
                  "------------------------------\n")

            #Calculate payment values
            #Note: calculate_from_salary function tuple value order is salary_portion, superannuation, paycycle_tax, net_salary_portion
            payment_values = paymod.calculate_from_salary(position, paycycle)            
            
            #Append values to lists
            first_names_list.append(first_name)
            last_names_list.append(last_name)
            positions_list.append(position)
            salaries_list.append(paymod.employee_pay_details(position)[0])
            gross_incomes_list.append(payment_values[0])
            net_incomes_list.append(payment_values[3])
            taxes_list.append(payment_values[2])
            supers_list.append(payment_values[1])

            #Set unused values to defaults to prevent errors (e.g. hours worked in pay cycle)
            #Paycycle * 38 means how many weeks worked as standard 38 hour work week
            hours_list.append(paycycle * 38)
            overtime_hours_list.append(0)
            holiday_hours_list.append(0)
        
    else:
        print("Please enter a valid input.\n")
        print("Press any key to quit.")
        wait_to_close()

    #Print payroll summary to Shell output
    print("------------------------------\n"
          "|       Payroll Summary      |\n"
          "------------------------------\n")
    print("Number of employees for pay cycle: {} person(s)".format(num_employees))
    print("Pay cycle: {} week(s)\n".format(paycycle))
    print("------------------------------\n")

    for x in range(num_employees):
        print(last_names_list[x] + ", " + first_names_list[x])
        print(positions_list[x])
        print("Annual salary: ${:.2f}".format(salaries_list[x]))
        print("")
        print("Standard hours worked: {:.2f}\nOvertime hours worked: {:.2f}\nHoliday hours worked: {:.2f}".format(hours_list[x], overtime_hours_list[x], holiday_hours_list[x]))
        print("")
        print("Gross income:            ${:.2f}".format(gross_incomes_list[x]))
        print("Superannuation withheld: ${:.2f}".format(supers_list[x]))
        print("Tax payable:             ${:.2f}".format(taxes_list[x]))
        print("")
        print("Net income:              ${:.2f}".format(net_incomes_list[x]))
        print("\n"
              "------------------------------\n")

    #Print payroll summary to text file
    with open('payroll.txt', 'w') as file:
        file.write("------------------------------\n"
                   "|       Payroll Summary      |\n"
                   "------------------------------\n\n")
        file.write("Number of employees for pay cycle: {} person(s)\n".format(num_employees))
        file.write("Pay cycle: {} week(s)\n\n".format(paycycle))
        file.write("------------------------------\n\n")

        for x in range(num_employees):
            file.write(last_names_list[x] + ", " + first_names_list[x] + "\n")
            file.write(positions_list[x] + "\n")
            file.write("Annual salary: ${:.2f}\n\n".format(salaries_list[x]))
            file.write("Standard hours worked: {:.2f}\nOvertime hours worked: {:.2f}\nHoliday hours worked: {:.2f}\n\n".format(hours_list[x], overtime_hours_list[x], holiday_hours_list[x]))
            file.write("Gross income:            ${:.2f}\n".format(gross_incomes_list[x]))
            file.write("Superannuation withheld: ${:.2f}\n".format(supers_list[x]))
            file.write("Tax payable:             ${:.2f}\n\n".format(taxes_list[x]))
            file.write("Net income:              ${:.2f}".format(net_incomes_list[x]))
            file.write("\n\n"
                       "------------------------------\n\n")
            
    print("Press any key to quit.")
    wait_to_close()
    
elif menu_select == "P":
    try:
        #Print from txt file to Shell -- last user session
            #Original print function, removed and rewritten to add formatting
            #with open('payroll.txt', 'r') as file:
                #file_lines = re.sub(r'\n+', '\n', file.readlines())

                #for line in file_lines:
                    #print(line)
        
        #Writes file contents to list
        with open('payroll.txt', 'r') as file:
            file_lines = file.readlines()

        for line in file_lines:
            line = re.sub(r'\n', '', line)
            line = re.sub(r'\n\n\n', '\n\n', line)
            
            print(line)
            
    except Exception as e:
        print(e)
        print("\nThere is either no file named 'payroll.txt' or previous payroll session or both.")
    
    print("Press any key to quit.")
    wait_to_close()
    
elif menu_select == "H":
    print("------------------------------\n"
          "|         Help Manual        |\n"
          "------------------------------\n")
    
    print("Assumptions:\n"
          " 1. Superannuation is calculated at a rate of 10% gross income \n    (pre-tax amount)\n"
          " 2. Tax is calculated at the rates of the 2021–2022 financial year\n"
          " 3. Managers receive an average annual salary of $180 000\n"
          " 4. Senior Software Developers receive $150 000, \n    Mid-level Software Developers $130 000, and \n    Junior Software Developers $80 000 as their respective annual salary\n"
          " 5. Employees work for a maximum of 38 hours per week \n    (excluding overtime and other reasonable additional hours)\n"
          " 6. The hourly rate for the employees will be \n    calculated based on Assumption 4\n"
          " 7. All employees work for 50 weeks of the year\n"
          " 8. Employees who work on public holidays get paid double time \n    for the hours they worked on that specific day\n"
          " 9. Employees who work overtime get paid time-and-a-half \n    for the hours they worked overtime on that specific day\n")

    print("For more help, please consult the user manual at:\n"
          "https://github.com/Kridtity/BlackHatPayroll/blob/main/README.md\n")

    print("Enter \"OPEN\" to open the link or press any key to quit.")

    i = input("").upper()
    
    if i == "OPEN":
        webbrowser.open('https://github.com/Kridtity/BlackHatPayroll/blob/main/README.md')
    else:
        quit()
    
elif menu_select == "S":
    print("------------------------------\n"
          "|          Settings          |\n"
          "------------------------------")
    
    #Default values for reference
    #DEV_MANAGER_SALARY = 180000
    #SENIOR_DEV_SALARY = 150000
    #MID_DEV_SALARY = 120000
    #JUNIOR_DEV_SALARY = 80000

    #Gets current salaries
    with open('salaries.txt', 'r') as file:
        file_lines = file.readlines()

        #Print current settings
        print("Current salaries for positions:")
        print("Software Development Manager: {}"
              "Senior Software Developer: {}"
              "Mid-level Software Developer: {}"
              "Junior Software Developer: {}\n".format(file_lines[0], file_lines[1], file_lines[2], file_lines[3]))
        
    while True:
        menu_select = input("Enter: E => Edit salary details\n"
                            "       S => Save and go back to main menu\n"
                            "       D => Reset values to default\n").upper()
          
        if menu_select == "E":
            print("Enter custom salary values.")

            #Gets new salary input
            DEV_MANAGER_SALARY = int(input("Software Development Manager: "))
            SENIOR_DEV_SALARY = int(input("Senior Software Developer: "))
            MID_DEV_SALARY = int(input("Mid-level Software Developer: "))
            JUNIOR_DEV_SALARY = int(input("Junior Software Developer: "))

            #Writes custom salaries to salaries.txt
            with open("salaries.txt", 'w') as file:
                #Erases file contents
                file.truncate(0)
                file.writelines([str(DEV_MANAGER_SALARY) + "\n", str(SENIOR_DEV_SALARY) + "\n", str(MID_DEV_SALARY) + "\n", str(JUNIOR_DEV_SALARY)])
                               
        elif menu_select == "S":
            #Reloads the module
            importlib.reload(payroll)

        elif menu_select == "D":
            #Opens salaries.txt or creates it, assigning default (assumed salaries)
            with open("salaries.txt", 'w') as file:
                file.truncate(0)
                file.writelines(["180000\n", "150000\n", "120000\n", "80000"])

        else:
            print ("Please enter a valid input.\n")
            continue
                       
                
elif menu_select == "E":
    quit()
 
elif menu_select == "42":
    #A random piece of culture
    print("You found the Answer to the Ultimate Question of Life, The Universe, and Everything\n")
    print("Press any key to quit.")
    wait_to_close()
    
else:
    print("Please enter a valid input.\n")
    print("Press any key to quit.")
    wait_to_close()
