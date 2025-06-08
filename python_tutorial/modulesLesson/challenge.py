from functions import *

account = int(input("1 - Run 2 - Quit: "))
while account != 2:
    
    employee = input("Enter the name of the Employee: ")
    employee_type = input("Salary or Hourly: ").lower()
    
    if employee_type == 'hourly':
        time = int(input("Hours worked this month: "))
        pay = part_time(time)
    elif employee_type == 'salary':
        exp = int(input("Years on the job: "))
        pay = full_time(exp)
    else:
        print("You don't have a job...")
    print(employee, " - salary of: ", pay)
    account = int(input("1 - Run 2 - Quit: 1"))