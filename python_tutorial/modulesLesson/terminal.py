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