class Animal():
    def __init__(self, name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound
        
    def speak(self):
        print(self.sound)
        
    def pet_info(self):
        print("My", self.pet, "has the name of ", self.name, "and they make the sound of", self.sound)
        
class Fish(Animal):
    def swim(self):
        if self.sound == None:
            print("You are a fish")
        else:
            print("You must not be a fish")
            
    def ocean(self):
        region = input("Enter an ocean: ")
        print(self.name, "is a",self.pet, "who lives in",region,"ocean")
        
memo = Fish("memo","Fish","None")

# memo.speak()
# memo.pet_info()

memo.swim()
memo.ocean()        