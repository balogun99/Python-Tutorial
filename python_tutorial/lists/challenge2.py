cities = list()
city = input("Enter a city: ").lower()

while city != '0':
    if city in cities:
        print("You've already entered that city")
    else:
        cities.append(city)
    city = input("Enter a city: ").lower()
cities.sort()
print("Lists of cities: ", cities)

# Stopped 09:55mins:26secs