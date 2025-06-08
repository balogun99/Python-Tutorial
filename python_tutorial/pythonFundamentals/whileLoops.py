# While loop
# 
password = input("Enter your password: ")
while password != 'balogun1999':
    print("You entered the wrong password!")
    password = input("Try again: ")
print("Welcome to your account!")
# 

# 
cost = int(input("Enter the cost of an item (0 to an end): "))
total = 0
while cost != 0:
    total += cost
    cost = int(input("Enter the cost of an item (0 to an end): "))
    print("Grand Total: ", total)
    total = total * 0.50
    print("Total price with discount: ", total)  
# 

#    
message = input("Enter message: ")
while message != 'done':
    print("We got your message!")
    message = input("Enter your message: ")

password = input("Enter your password: ")
while password != 'balogun' and password != 'ishaq':
    password = input("Wrong password, Try again!")
print("Welcome to your account!")
# 

# 
counter = 0
while counter < 3:
    name = input("Enter your name: ")
    print("Congrats! ", name, "You saved 20%")
    counter += 1
print("All done!")
# 

# 
tries = 0
code = ""

while tries < 5 and code != "python":
    code = input("Enter a programming language: ")
    tries += 1
if code == "python":
    print("It took you", tries, "trials")
# 

# 
train_tickets = input("0 - to get ticket, 1 - end booking: ")
i = 1
while train_tickets != '1':
    if train_tickets == '0':
        print("Train Ticket: ", str(i))
        i += 1
    train_tickets = input("0 - to get ticket, 1 - turn off device: ")
# 