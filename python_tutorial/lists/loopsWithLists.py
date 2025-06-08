ages = list()
age = int(input("Enter an age: "))

minors = 0
seniors = 0

while age != 0:
    for age in ages:
        if age < 18:
            minors += 1
        elif age >= 70:
            seniors += 1
        ages.append(age)
        
    age = int(input("Enter an age: "))
    
print("All the ages: ", ages)
print("Number of minors: ", minors, " - Number of seniors: ", seniors)