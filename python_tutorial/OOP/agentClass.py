class Agent():
    def __init__(self, name, health, car):
        self.name = name
        self.health = health
        self.car = car
        
    def player_info(self):
        print("Welcome, ", self.name)
        print("Your Health: ", self.health)
        print("Your car is: ", self.car)
        
spy = Agent("Ethan Hunt", 100, "Jaguar")
villain = Agent("James Bond", 45, "Ferrari")

spy.player_info()
villain.player_info()