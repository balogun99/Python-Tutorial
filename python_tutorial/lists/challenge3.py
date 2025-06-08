from random import *

players = input("Enter each player name: ").split(" ")
player_amt = len(players)

team = list()
for player in players:
    random_team =  randint(1,3)
    team.append(random_team)
    
for i in range(player_amt):
    print(players[i], "-", team[i])