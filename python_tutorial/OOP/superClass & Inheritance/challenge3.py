from time import sleep

class Agent():
    def __init__(self, name, health, car):
        self.name = name
        self.health = health
        self.car = car
        
    def agent_info(self):
        print("Welcome: ", self.name)
        print("Your health is: ", self.health)
        print("Car choice is: ", self.car)
          
class Spy(Agent):
    def __init__(self, name, health, car, agency, location):
        super().__init__(name, health, car)
        self.agency = agency
        self.location = location
        self.killed = False
        
    def assassinate(self, bad_guy):
        if bad_guy.health > 0:
            bad_guy.health -= 20
            print(bad_guy.name, "has lost 20 from their health")
            print(bad_guy.name, "has the health of", bad_guy.health)
            if bad_guy.health <= 0:
                self.killed = True
                print(bad_guy.name, "is dead...", self.killed)
        
james_bond = Spy("James Bond", 100, "Jaguar", "MI6", "London")
ethan_hunt = Spy("Ethan Hunt", 40, "Ferrari", "CIA", "Dubai")

james_bond.agent_info()
ethan_hunt.agent_info()

sleep(5)

while ethan_hunt.health > 0:
    james_bond.assassinate(ethan_hunt)
    ethan_hunt.assassinate(james_bond)
    sleep(2)