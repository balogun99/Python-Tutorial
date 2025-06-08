# for loop // For every element in this variable, do something with it

username = input("Enter username: ")
invalid = "!@#$%^&*()_+?"
for letter in username:
    if letter in invalid:
        print("This character is not allowed: ", letter)

for i in range(5):
    number = input("Enter a number: ")
    print("Number added: ", number)
print("All 5 numbers added")

passengers = int(input("How many passengers ?: "))
for i in range(passengers):
    lastName = input("Enter a Last Name: ")
    print("Hello: ", lastName)
print("Passengers manifest updated!")

password = input("Enter your password: ")
invalid = "!@#$%^&*()_+"
for letter in password:
    if letter in invalid:
        print("Invalid Password, try again!", letter)

vowels = 'aeiou'
const = 'bcdfghjklmnpqrstvwxyz'

word = input("Enter any word: ")
vowel_num = 0
for letter in word:
    if letter in vowels:
        vowel_num += 1
    elif letter in const:
        vowel_num += 0
print("There are: ", vowel_num, "vowels in the word")

phoneNumber = input("Enter your phone number: ")
validNumber = '0123456789'

for number in phoneNumber:
    if number not in validNumber:
        print("Not a valid number")

guests = int(input("Enter the number of guests: "))
for i in range(guests):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Welcome, ", name)
    else:
        print("You must be 18 to drink")

for i in range(5):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "12345":
        print("Welcome to your account", username, "admin")
        break
        
if username != "admin" and password == "12345":
        print("You're not an admin!")

# stopped at 4:00:15