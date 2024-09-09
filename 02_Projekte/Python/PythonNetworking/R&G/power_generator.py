import random

power_list = ["superspeed", "superpower", "invisibility"]

def pwr_gen():
    number = random.randint(1, 2)
    return number

def check_number(number):
    power = ""
    match number:
        case 1:
            power = "superspeed"
        case 2:
            power = "superpower"
    return power

power = check_number(pwr_gen())
print(power)