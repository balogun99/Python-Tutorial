class Agent():
    def __init__(self, name, health, car):
        self.name = name
        self.health = health
        self.car = car
        
    def player_info(self):
        print("Welcome: ", self.name)
        print("Your health is :", self.health)
        print("Your car choice is: ", self.car)

class Spy(Agent):
    def __init__(self, name, health, car, location, agency):
        super().__init__(name, health, car)
        self.location = location
        self.agency = agency
        
    def spy_talk(self):
        print("My name is: ",self.name)
        print("I based at", self.agency, "in", self.location)
        
james_bond = Spy("James Bond", "100", "Jaguar", "London", "MI6")
james_bond.spy_talk()