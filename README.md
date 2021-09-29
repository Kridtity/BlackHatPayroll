# BlackHat Payroll Program
## Description
This Year 11 Computer Science ATAR project is a payroll program system for hypothetical company 'BlackHat IT'. It accepts inputs for employee details such as name, position, and hours worked to calculate the payroll information for the employee for the input pay cycle. Payroll information output from the program includes: assumed salary based on job position, standard hours worked, overtime hours worked, holiday hours worked and gross income, superannuation withheld, tax payable, and net income for the input pay cycle.

## User Manual
### Contents
1. [Part A](#part-a)
   + [Assumptions](#assumptions)
2. [Part B](#part-b)
   + [Main Menu](#main-menu)
     + [I => Input employee pay details](#i--input-employee-pay-details)
     + [P => Print last payroll session in IDLE Shell/command line](#p--print-last-payroll-session-in-idle-shellcommand-line)
     + [H => Help manual](#h--help-manual)
     + [E => Exit the program ](#e--exit-the-program)
   + [Input employee pay details menu](#input-employee-pay-details-menu)
     + [H => Calculate payroll based on hourly rate and hours worked](#h--calculate-payroll-based-on-hourly-rate-and-hours-worked)
     + [S => Calculate payroll based on annual salary](#s--calculate-payroll-based-on-annual-salary)

## Part A:
### Assumptions:
1. Superannuation is calculated at a rate of 10% gross income (pre-tax amount)
2. Tax is calculated at the rates of the 2021–2022 financial year
3. Managers receive an average annual salary of $180 000
4. Senior Software Developers receive $150 000, Mid-level Software Developers $130 000, and Junior Software Developers $80 000 as their respective annual salary
5. Employees work for a maximum of 38 hours per week (excluding overtime and other reasonable additional hours)
6. The hourly rate for the employees will be calculated based on Assumption 4
7. All employees work for 50 weeks of the year
8. Employees who work on public holidays get paid double time for the hours they worked on that specific day
9. Employees who work overtime get paid time-and-a-half for the hours they worked overtime on that specific day


## Part B:
### Main Menu
The main menu provides four options for the selection of the main functionality of the program:
1. I => Input employee pay details
2. P => Print last payroll session in IDLE Shell/command line
3. H => Help manual
4. E => Exit the program  

#### I => Input employee pay details
This option allows the user of the program to calculate the payroll by being prompted for inputs on employee details, the pay cycle the program is supposed calculate using (in weeks), and the employees' work details (e.g. how many hours did they work in the selected pay cycle).

Typing the letter 'I' results in another menu being displayed providing the options of calculating the payroll using assumed hourly rates (for standard, overtime, and holiday hours calculated from the assumed annual salary of each employee based on ), and the number and type of hours worked by each employee; or calculating the payroll based on an assumed annual salary for each employee job position and the number of weeks in the chosen pay cycle (each week is assumed to to contain 38 hours of standard work).

#### P => Print last payroll session in IDLE Shell/command line
This option prints the last payroll session saved in the 'payroll.txt' file into the the IDLE Shell/command line. If there is no file or previous payroll session, an exception will be thrown and error printed to the IDLE Shell/command line.

#### H => Help manual
This option prints the list of [Assumptions](#assumptions) and a link to [this](https://github.com/Kridtity/BlackHatPayroll/blob/main/README.md) user manual and option to open in browser if more help is required.

#### E => Exit the program 
This option attempts to quit the program, either immediately closing it or displaying a prompt asking for confirmation to kill the program.


### Input employee pay details menu
Two options are available in this menu:
1. H => Calculate payroll based on hourly rate and hours worked
2. S => Calculate payroll based on annual salary

Whichever option chosen, the prompt 'Enter pay cycle in full weeks' refers to the number of full weeks in the chosen pay cycle, and the prompt 'Enter number of employees' refers to the number of employees who worked or are to be payed in/during/for the input pay cycle.

#### H => Calculate payroll based on hourly rate and hours worked
This option is used for calculating the payroll during a pay cycle in which employees do not work the assumed standard 38 hours per week. It is used for calculating payrolls when employees work for more or less than 38 hours per week or the selected pay cycle equivalent, or if any employees have worked overtime or holiday hours during the pay cycle.

#### S => Calculate payroll based on annual salary
This option is used for calculating the payroll when all employees worked 38 standard hours per week or their pay cycle equivalent. Overtime and holiday hours worked are not factored into calculations under this option.
