import random
from tkinter.font import names
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

random_name = random.choice(names)

print("The selected random name is:", random_name)