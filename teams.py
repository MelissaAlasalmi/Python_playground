import random

names = ["Ben", "Melissa", "Joe", "Lizzo", "Fred", "Bob"]
teams = ["red", "blue", "green"]

#Randomly assigns everyone in 'names' a team from 'teams'
for name in names:
    print("Hello, " + name + "! You are on team " + random.choice(teams) + "!") 
