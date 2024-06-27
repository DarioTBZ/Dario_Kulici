import time
def dprint(string):
   for letter in string:
        __builtins__.print(letter,end = '', flush=True)
        time.sleep(0.04)
   __builtins__.print("")

print = dprint


# Variabeln
active = True
kohlenhydrate = 0
menge_in_gramm = 0


print("Willkommen zum Kohlenhydraterechner für Diabetiker!\n")
while active == True:
    print("\nKohlenhydrate angeben. (Achtung, nicht davon Zucker)")
    try:
        kohlenhydrate = float(input("Kohlenhydate: "))
    except ValueError:
        print("\nBitte gib eine gültige Zahl ein.\n")
        continue
    print("Gut! Jetzt brauchen wir nur noch die Gramm Menge von der Packung!\n")
    try:
        menge_in_gramm = float(input("gramm: "))
    except ValueError:
        print("\nBitte gib eine gültige Zahl ein.\n")
        continue

    anzahl_wert = float(menge_in_gramm) / (1000 / float(kohlenhydrate))
    print("\nDie Packung hat " + str(anzahl_wert) + " Wert bei " + str(kohlenhydrate) + "g Kohlenhydrate\n")
    print("Drücke enter, um fortzufahren oder tippe (stop), um das Programm zu schliessen")
    runagain = input(": ")
    if runagain == "stop":
        active = False
    else:
        active = True