from bmiFunctions import show_results

people = int(input("Enter the number of people: "))
for i in range(people):
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    show_results(weight, height)