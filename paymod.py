#Author: Kridtity Ikhlaas Lawang
#Program Name: paymod

#License: GNU GPLv3.0
#Status: Release
#Version: 1.0
#Release Date: 29-11-2021
#Description: Module for payroll calculation system for Blackhat IT

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

#Formulas:
#Calculate superannuation: value * 0.1
#Convert annual value to pay cycle value: value * (paycycle / 50)

#Import modules
import math
import re

#Function to calculate wage and other financial details based on hourly rates
def calculate_from_wage(position, paycycle, hours_worked, overtime_hours_worked, holiday_hours_worked):
    #Gets employee pay details based on passed position
    salary = employee_pay_details(position)[0]
    hourly_rate = employee_pay_details(position)[1]
    overtime_rate = employee_pay_details(position)[2]
    holiday_rate = employee_pay_details(position)[3]

    #Calculates wages based on hourly input
    wage = float((hourly_rate * hours_worked) + (overtime_rate * overtime_hours_worked) + (holiday_rate * holiday_hours_worked))

    #Calculates superannuation for pay cycle based on wage (rate at 10% pre-tax amount)
    superannuation = float(wage * 0.1)

    #Calculates tax withheld from pay cycle
    paycycle_tax = float(calculate_tax_from_wage(wage, paycycle))

    #Calculates net wage
    net_wage = float(wage - superannuation - paycycle_tax)
    
    return wage, superannuation, paycycle_tax, net_wage


#Function to calculate salary portion recieved in the pay cycle and other financial details based annual salary
def calculate_from_salary(position, paycycle):
    #Gets employee pay details based on passed position
    salary = employee_pay_details(position)[0]
    
    #Gets employee salary portion for pay cycle
    salary_portion = float(salary * (paycycle / 50))

    #Calculates superannuation for pay cycle based on wage (rate at 10% pre-tax amount)
    superannuation = float(salary_portion * 0.1)

    #Calculates tax * (pay cycle / 50) for pay cycle based on annual salary
    gross_tax = float(calculate_tax_from_salary(salary))
    paycycle_tax = float(gross_tax * (paycycle / 50))

    #Calculates net salary portion
    net_salary_portion = float(salary_portion - superannuation - paycycle_tax)
    
    return salary_portion, superannuation, paycycle_tax, net_salary_portion
    
    
#Function to calculate tax from salary
def calculate_tax_from_salary(salary):
    #Algorithm for calculating tax according to income bracket
    if salary >= 0 and salary <= 18200:
        tax = 0
    elif salary >= 18201 and salary <= 45000:
        tax = float(0.19 * (salary - 18200))
    elif salary >= 45001 and salary <= 120000:
        tax = float(5092 + (0.325 * (salary - 45000)))
    elif salary >= 120001 and salary <= 180000:
        tax = float(29467 + (0.37 * (salary - 120000)))
    elif salary >= 180001:
        tax = float(51667 + (0.45 * (salary - 180000)))  
    else:
        tax = 0

    return tax


#Function to calculate tax withheld from wage
def calculate_tax_from_wage(wage, paycycle):
    #Calculates average wage per week by dividing floored wage for pay cycle by weeks in pay cycle + 99 cents
    weekly_income = float(math.floor(wage / paycycle) + 0.99)

    if weekly_income < 88:
        a = 0.1900
        b = 0.1900
    elif weekly_income < 371:
        a = 0.2348
        b = 3.9639
    elif weekly_income < 515:
        a = 0.2190
        b = -1.9003
    elif weekly_income < 932:
        a = 0.3477
        b = 64.4297
    elif weekly_income < 1957:
        a = 0.3450
        b = 61.9132
    elif weekly_income < 3111:
        a = 0.3900
        b = 150.0093
    elif weekly_income >= 3111:
        a = 0.4700
        b = 398.9324
    else:
        a = 0
        b = 0

    tax_withheld = float(((a * weekly_income) - b) * paycycle)

    return tax_withheld

    
#Function to get employee salary and rates (38 * 50 is 38 hrs per week, 50 weeks to get hourly rate)
def employee_pay_details(position):
    with open('salaries.txt', 'r') as file:
        file_lines = file.readlines()

        for line in file_lines:
            line = re.sub(r'\n', '', line)

    #Converts position to lower for easier parsing
    #Consider making strict list of positions -- nah, too lazy
    position = position.lower()

    #Assigns salry based on position
    #If CEO like me or MS, then salary is $4B
    if position == "undaunted" or position == "frazebean":
        salary = 4000000000
    elif "manager" in position:
        salary = float(file_lines[0])
    elif "senior" in position:
        salary = float(file_lines[1])
    elif "mid" in position:
        salary = float(file_lines[2])
    elif "junior" in position:
        salary = float(file_lines[3])
    else:
        salary = 0

    #Calculates different hourly rates based on salary
    hourly_rate = float(salary / (38 * 50))
    overtime_rate = float(hourly_rate * 1.5)
    holiday_rate = float(hourly_rate * 2)
    return salary, hourly_rate, overtime_rate, holiday_rate
