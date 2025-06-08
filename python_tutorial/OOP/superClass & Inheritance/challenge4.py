class Player():
    def __init__(self, name, age, club, nationality):
        self.name = name
        self.age = age
        self.club = club
        self.nationality = nationality
        
    def player_info(self):
        print("Welcome, your name is: ", self.name)
        print("Your age is: ", self.age)
        print("And your club is: ", self.club)
        print("Your are from: ", self.nationality)
        
class Profile(Player):
    def __init__(self, name, age, club, nationality ,jersey_number, position):
        super().__init__(name, age, club, nationality)
        self.jersey_number = jersey_number
        self.position = position
        
    def get_age(self):
        if self.age == 18:
            return "Academy Player"
        elif self.age >= 25:
            return "First Team Player"
        else:
            return "Retired Player"
        
    def get_team(self):
        if self.club == "Arsenal" and self.club == "Manchester City" and self.club == "Liverpool" and self.club == "Chelsea":
            return "Big Club"
        else:
            return "Average Club"
        
    def get_nationality(self):
        if self.nationality == "Europe" and self.nationality == "Asia" and self.nationality == "America":
            return "You're from Europe/America or Asia"
        else:
            return "You're from Africa"
        
    def input_details(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        club = input("What's your club: ")
        nationality = input("Which nationality are you from? (Europe/America or Asia): ").lower()
 
player_details = Profile("James Bond", 24, "Arsenal", "Nigeria", 7, "Midfield")

player_details.input_details()
# player_details.player_info()

print(player_details.get_team())
print(player_details.get_age())
print(player_details.get_nationality())