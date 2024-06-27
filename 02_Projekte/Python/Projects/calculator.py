import math

# Variables
calculationtype_user = "";
active = 1;
first_number = 0;
second_number = 0;
sum = 0;
help = """\nDieser Rechner hat Standard Rechenfunktionen (+, -, *, /) und alle weiteren sind aufgelistet:
    - Square Root
        \n"""
goodinput = 0
sqrt_on = 0


# Mainloop
while active == 1:
    print("Wie soll gerechnet werden? Gib (stop) ein, um das Programm zu beenden oder tippe (help), um weitere Möglichkeiten anzuzeigen.")

    calculationtype_user = input("\n+-*/: ")

    # Special commands
    if calculationtype_user == "stop":
        break
    if calculationtype_user == "help":
        print(help)
        input("Drücke Enter, fortzufahren...\n")
        continue
    if calculationtype_user == "sqrt":
        sqrt_on = 1

    # Goodinput Check
    if (calculationtype_user == "+") or (calculationtype_user == "-") or (calculationtype_user == "*") or (calculationtype_user == "/") or (calculationtype_user == "sqrt"):
        goodinput = 1
    else:
        print("Fehler: Ungültiger Input.\n")
        goodinput = 0
        continue
    
    # input (mainprogramm)
    if goodinput == 1 and sqrt_on == 0:
        first_number = input("Erste Zahl: ")
        second_number = input(first_number + " " + calculationtype_user + " ")
    if sqrt_on == 1:
        first_number = input("Zahl von der die Wurzel genommen wird: ")
        
    
    if goodinput == 1:
        if calculationtype_user == "+":
            sum = float(first_number) + float(second_number)
        if calculationtype_user == "-":
            sum = float(first_number) - float(second_number)
        if calculationtype_user == "/":
            sum = float(first_number) / float(second_number)
        if calculationtype_user == "*":
            sum = float(first_number) * float(second_number)
        if calculationtype_user == "sqrt":
            sum = math.sqrt(float(first_number))



    if goodinput == 1:
        print("Das Ergebnis ist " + str(sum))
        sum = 0
        calculationtype_user = ""

else:
    active = 0