def terminal_1():
    print("Departing from Terminal 1 - Budget")
    flight_check()
    
def terminal_2():
    print("Departing from Terminal 2 - Domestic")
    flight_check()
    
def terminal_3():
    print("Departing from Terminal 3 - International")
    flight_check()
    
    
def flight_check():
    answer = input("Budget/Domestic or International: ").lower()
    if answer == 'budget':
        terminal_1()
    elif answer == 'domestic':
        terminal_2()
    elif answer == 'international':
        terminal_3()
    else:
        print("There is no other terminal")
        
flight_check()

# Challenge 4

def calculate_bmi(weight, height):
    calculation = weight / (height * height)
    return calculation

def show_results(weight, height):
    calculation = calculate_bmi(weight, height)
    if calculation <= 18.5:
        print("Underweight")
    elif calculation > 18.5 and calculation <= 25:
        print("Normal")
    else:
        print("Overweight")
        
people = int(input("Enter the number of people: "))
for i in range(people):
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    show_results(weight, height)