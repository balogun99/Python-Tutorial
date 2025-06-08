answers = list()
fruit = input("Enter the name of a fruit: ")
while fruit != 'quit':
    answers.append(fruit)
    fruit = input("Enter the name of a fruit: ")

guess = input("Guess a fruit: ").lower()
for answer in answers:
    if guess == answer:
        print("Congrats!!, you got it!.")
        break
    else:
        print("You guess it wrong")
        break