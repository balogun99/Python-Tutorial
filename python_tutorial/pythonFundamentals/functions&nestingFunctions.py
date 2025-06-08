rentalPrice = int(input("Enter the rental price per day: "))
days = int(input("Enter the number of days to rent: "))

total = rentalPrice * days
print("Total car price is: ", total)


package1 = int(input("Enter the weight of package1: "))
package2 = int(input("Enter the weight of package2: "))
package3 = int(input("Enter the weight of package3: "))
print("The shipment total is: ", (package1 + package2 + package3) * 0.8)

# Coding Challenge 1

userIncome = int(input("Enter your monthly income: "))

foodExpenses = int(input("Enter the expenses for food: "))
houseRent = int(input("Enter your house rent: "))
extra = int(input("Enter other extra expenses: "))

remaining = userIncome - foodExpenses - houseRent - extra

print("The remaining total left after income is: ", remaining)