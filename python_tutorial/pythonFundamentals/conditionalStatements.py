tripType = input("Is your trip business/leisure or personal ?: ").lower()
tripCost = int(input("Enter trip expected cost: "))

discount = tripType == 'business' and tripCost >= 1200
print("The customer receives a discount of :", discount)

password = input("Enter your password: ")

if password == "ishaqjnr1999":
    print("correct password")
else:
    print("incorrect password")

cost = int(input("Enter your trip funds: "))

if cost < 350:
    print("Go on a stay-cation")
if cost >= 350 and cost < 1000:
    print("Go on a Road Trip")
if cost >= 1000:
    print("Pack your bags, and a catch a flight to the beach")
    
print("Have Fun")

bagWeight = int(input("Enter the bag weight in KG: "))
destination = input("Domestic or International ?: ")

if bagWeight <= 18:
    price = 25
else:
    price = 75

if destination == 'Domestic':
    price = price + 300
elif destination == 'International':
    price += 750
else:
    print("Spelling Error")
    
print("The ticket price is: ", price)