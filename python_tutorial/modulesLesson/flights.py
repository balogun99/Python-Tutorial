from terminal import *

question = input("Would you like to check your flight?: ").lower()
while question != 'quit':
    if question == 'yes':
        flight_check()
    else:
        print("You did not say yes")
    question = input("Would you like to check your flight?: ").lower()
    