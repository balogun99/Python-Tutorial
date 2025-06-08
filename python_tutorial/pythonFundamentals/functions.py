def person_info (name, age, nationality):
    print("Welcome: ", name)
    print("You are: ", age)
    print("You are from: ", nationality)

# print(person_info())

number = int(input("Amount: "))
for i in range(number):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    nationality = input("Enter your nationality: ")
    
    person_info (name, age, nationality)
    
def total_points(game_score):
    points = 0
    while game_score != 0:
        if game_score >= 5 and game_score <= 10:
            points += 2
            if game_score > 10 and game_score <= 20:
                points += 3
        game_score = int(input("Enter the game score: "))
    return points

score = int(input("Enter the score: "))
game_points = total_points(score)
print(game_points)

def good_deal(cost):
    if cost >= 50 and cost < 150:
        response = 'This is a good deal'
    elif cost >= 150:
        response = 'Overpriced'
    else:
        response = 'Cheap, buy now'
        
    return response

store = input("Enter the store name: ")
cost = float(input("Enter the cost: "))

response = good_deal(cost)
print(store, "-", response)

if response == 'This is a good deal':
    print("Buy before its too late")

# Challenge 1

def grade(score):
    print("Your score is: ", score)
    if score > 0 and score <= 50:
        print("Below passing, improve your score")
    elif score > 50 and score <= 70:
        print("Barely passing the class")
    elif score > 70 and score <= 90:
        print("You have a passing grade")
    else:
        print("You are one of the best in the class")
        
score = int(input("Enter your score: "))
grade(score)

# Challenge 2

def flight_charges(price):
    upgrade = input("Would you like to upgrade?: ")
    if upgrade == 'yes':
        price += 99
    baggage = input("Will you have baggage?: ")
    if baggage == 'yes':
        price += 35
        
    tax = (price * 0.08) + price
    return tax

price = int(input("Enter your base fare: "))
grand_total = flight_charges(price)
print("The Grand Total after Tax is: ", grand_total)

# Challenge 3

def bank_balance(balance):
    if balance >= 500:
        return True
    else:
        return False
    
bankers = int(input("Number of bank customers: "))
for i in range(bankers):
    full_name = input("Your Full Name: ").capitalize()
    balance = float(input("Your Bank Balance: "))
    response = bank_balance(balance)
    
    print("Enough funds in " + full_name + "'s account: " , response)
    if response == True:
        print("Don't worry, enough funds!")
    else:
        print("Your account is getting low.")

def mortgage(cash):
    if cash >= 50000:
        print("Instant Approval")
    elif cash < 50000 and cash > 20000:
        print("You need an approval")
    else:
        print("Not approved for mortgage yet")
        
cash = int(input("Deposit Amount: "))
total_balance = 0

while cash != 0:
    total_balance += cash
    mortgage(cash)
    cash = int(input("Deposit Amount: "))
print("Total money requested is: ", total_balance)

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
    calculate = calculate_bmi(weight, height)
    if calculate <= 18.5:
        print("Underweight")
    elif calculate > 18.5 and calculate <= 25:
        print("Normal")
    else:
        print("Overweight")
        
people = int(input("Enter the number of people: "))
for i in range(people):
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    show_results(weight, height)
    

# stopped at 06hrs:00mins
