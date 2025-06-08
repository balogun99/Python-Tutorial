from random import randint

passenger = input("Enter passenger name (quit to quit): ")
while passenger != "quit":
    flight_number = randint(1,3)
    print(passenger, ",Flight Number is: ", flight_number)
passenger = input("Enter passenger name (quit to quit): ")

import random
winner = 365
current = random.randint(1,500)
print("Wining number: ", current)

if current == winner:
    print("You win a free trip")
else:
    print("You lost!")

from random import randint

flight_1 = 0
flight_2 = 0

ask = input("Would you like to book another flight?: ").lower()
while ask != 'no':
    flight_number = randint(1,2)
    print("Flight number: ", flight_number)
    if flight_number == 1:
        flight_1 += 1
    else:
        flight_2 += 1
    ask = input("Would you like to book another flight?: ").lower()
print("Number of passengers on flight 1:", flight_1)
print("Number of passengers on flight 2:", flight_2)

from random import *

guess = int(input("Guess any number between 1 - 10: "))
random_number = randint(1,10)

if guess < random_number:
    print("Too low")
elif guess > random_number:
    print("Too high")
else:
    print("Wow, you got it")

from random import *

guess = int(input("Guess any number between 1 - 10: "))
random_number = randint(1,10)

while guess != random_number:
    x = random_number
    tries = 1
    while x != guess:
        if guess < x:
            print("Too low!")
            tries += 1
        elif guess > x:
            print("Too high")
            tries += 1
        guess = int(input("Guess any number between 1 - 10: "))
        
    print("Congrats, you got it!")
    print("It took you: ", tries, "tries")
    
    # 06:47mins
    