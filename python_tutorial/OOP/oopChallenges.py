class Animal():
    def __init__(self, name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound
        
    def speak(self):
        print(self.sound)
        
    def pet_info(self):
        print("My",self.pet,"has the name",self.name,"they make the sound",self.sound)
        
dog = Animal("Max","Dog","Woof, Woof!")

cat = Animal("Andy","Cat","Meow Meow!")

dog.speak()
cat.speak() 

dog.pet_info()
cat.pet_info()

class Player():
    def __init__(self, name, goals):
        self.name = name
        self.goals = goals
        self.team = None
        
    def show_stats(self):
        print("Player: ", self.name)
        print("Goals: ", self.goals)
        print("Team: ", self.team)
        
    def select_team(self):
        team = input("Enter the team name: ")
        self.team = team
        
player = Player("Mohammed Salah", "9")
player.show_stats()

player.select_team()
player.show_stats()

class Coach():
    def __init__(self, name, club):
        self.name = name
        self.club = club
        self.age = None
        
    def show_details(self):
        print("Manager Name: ", self.name)
        print("Club: ", self.club)
        print("Your age is: ", self.age)
        
    def coach_details(self):
        age = input("What's your age: ")
        self.age = age
        
coach = Coach("Mikel Arteta", "Arsenal")
coach.show_details()

coach.show_details()
coach.coach_details()

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def print_info(self):
        print("Rectangle with the length of: ",self.length, "and with the width of: ",self.width)
        
    def calc_perimeter(self):
        self.perimeter = (self.length + self.width) * 2
        return self.perimeter
    
    def calc_area(self):
        self.area = self.length * self.width
        return self.area
    
    def update(self, length):
        self.updated = (self.length - length) * self.width
        return self.updated
    
a = int(input("Enter the length: "))
b = int(input("Enter the width: "))

rect = Rectangle(a,b)
rect.print_info()

print("Perimeter: ", rect.calc_perimeter())
print("Width: ",rect.calc_area())

c = int(input("Enter the number to subtract from the length: "))
print("Updated Area: ", rect.update(c))