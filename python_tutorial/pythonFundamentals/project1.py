print("Welcome to MiniChatBot 3.0. Let's plan your adventure")
enter = int(input("Enter 1 - to START or 2 - to QUIT: "))
while enter == 1:
    destination = input("Do you have a destination in mind ?. Yes or No: ").lower()
    if destination == 'yes':
        print("Let's plan your trip")
        transport = input("Choose transport: Plane/Train or Car: ").lower()
        if transport == 'plane':
            class_type = input("Which fare would you like? (Personal/Business/Economy)").lower()
            luggage = int(input("Enter the weight of your luggage (in KG): "))
            if luggage >= 21 and class_type == 'business' or class_type == 'personal':
                print("You can have more luggage of these classes")
            elif luggage < 21 and class_type == 'business' or class_type == 'personal':
                print("You can bring more luggage if you want")
            else:
                print("You may bring too much!")
        elif transport == 'train':
            seat_type = input("Economy or Business").lower()
            if seat_type == 'business':
                print("Great!. More comfort to your way")
            elif seat_type == 'economy':
                print("You save more this way")
            else:
                print("We don't have this class")
        elif transport == 'car':
            print("Road trips are FUN!")
            num_people = int(input("How many people?: "))
            if num_people <= 4:
                print("Great, you could rent a car")
            else:
                print("You may rent a van or a mini bus")
        else:
            print("We don't have that transport type...")
    
    else:
        print("I can help you choose a destination!")
        trip_type = input("Beach/City/Adventure: ").lower()
        if trip_type == 'beach':
            print("How about Hawaii")
            beach_type = input("Popular or remote beach: ").lower()
            if beach_type == 'popular':
                print("Check out Wakiki Beach near Honolulu")
            elif beach_type == 'remote':
                print("Head over to Maui")
            else:
                print("We don't have that option")
        elif trip_type == 'city':
            print("Head to New York City")
            activity = input("Indoor or Outdoor: ").lower()
            if activity == 'indoor':
                print("Check out the Met Museum")
            elif activity:
                activity == 'outdoor'
                print("Relax in Central Park")
            else:
                print("Wrong input, spelling error")
        elif trip_type == 'adventure':
            print("Head out to the National Park")
            outdoor_activity = input("Hiking or Camping?: ").lower()
            if outdoor_activity == 'hiking':
                print("Try Hiking Half Done")
            elif outdoor_activity == 'camping':
                print("Check out the many camping sites within the park")
            else:
                print("The activity is not offered")
        else:
            print("The print type is not available")
            
    print("Enter for a chance to win a FREE TRIP")
    for i in range(1,4):
        if input("What is the largest desert in the world? :") == 'antarctica':
            print("Wow!, you win a free trip")
            break
    enter = int(input("1 - START or 2 - STOP"))
print("Enjoy your trip")            