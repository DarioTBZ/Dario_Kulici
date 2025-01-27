import random
import json
import time

# Variabeln
active = 1
points = 0
active_points = "You have " + str(points) + " points."
ynroll = ""
lucky_number = 0
start = time.time()


def roll():
    lucky_number = (random.randint(1, 16))
    print(lucky_number)

def validate():
    global lucky_number
    global points
    lucky_number += points

while active == 1:
    print(active_points)
    print("Do you wanna roll? yes/no")
    ynroll = input()
    if ynroll == "no":
        end = time.time()
        online = float(start) - float(end)
        data = {
            "gathered points: " + str(points),
            "time online: " + str(online)
        }
        printdata = json.dumps(data)
        print(active_points)
        print(data)
        active = 0
    if ynroll == "yes":
        roll()
        validate()
    lucky_number = 0