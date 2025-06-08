ages = [18, 34, 55, 23]
age = int(input("Enter an age: "))

while age != 0:
    if age in ages:
        print("You've already entered that age")
    else:
        ages.append(age)
    age = int(input("Enter an age: "))
    
ages.sort()
print("List of ages in your lists: ", ages)