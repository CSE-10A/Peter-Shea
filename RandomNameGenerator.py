#Imported Random to pick a name from "names"
import random

names = [
    "Arjun",
    "Jerry",
    "Totti",
    "Ethan",
    "Jack",
    "Peter",
    "Nicholas",
    "Tony",
    "David",
    "Ollie",
    "Earl",
    "Andrew",
    "Alex",
]

while True:
    random.name = random.choice(names)

print("The selected random name is:", random.name)