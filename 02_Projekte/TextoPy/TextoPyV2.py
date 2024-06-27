# Variabeln
Level = 0
answer = ""

class Levels:
    class Level1:
        Level1 = "Wer war der erste Präsident Amerikas? Schreibe seinen ganzen Namen."
        Level1answer = "George Washington"
        Level1success = """
        Gut gemacht!
        """
    class Level2:
        Level2 = "Nun was ist der tiefste Ort der Erde? Schreibe den Namen."
        answerLevel2 = "Marianengraben"
        Level2success = """
        Wow, du bist echt gut!
        """
    class Level3:
        Level3 = "Wie lange Brauchen Ananas um zu wachsen? Schreibe die Zahl (Jahre)."
        Level3answer = "2"
        Level3success = """
        Du bist der nächste Champion wenn du so weiter machst!
        """
    Erfolg = """YUHEEE! Du hast das Quiz durchgespielt! Tippe: (again), um das Quiz neuzustarten!
    Falls du keine Lust mehr hast tippe: stop, um das Spiel zu beenden.
              """
    class Start: 
        Start = "Starte das Spiel indem du Start eingibst"
        Startanswer = "Start"
        Welcome = """Willkommen zu meinem Text-based-Spiel! Beantworte die Fragen und gewinne das Spiel!
              
              """
    
LevelEins = Levels.Level1.Level1
LevelZwei = Levels.Level2.Level2
LevelDrei = Levels.Level3.Level3

# Funktionen

def StartCheck():
    global Level
    global answer
    print("Willkommen zu meinem Spiel! Tippe (Start), um das Spiel zu beginnen!")
    answer = input("typeStart: ")
    if answer == Levels.Start.Startanswer:
        print(Levels.Start.Welcome)
        Level = 1
        ProgressTracker()
    else:
        return StartCheck()

def Abfrage():
    global answer
    answer = input("eingabe: ")
    Quit()

def checkAnswer():
    global Level
    if Level == 1 and answer == Levels.Level1.Level1answer:
        print(Levels.Level1.Level1success)
        Level = 2
        ProgressTracker()
    elif Level == 2 and answer == Levels.Level2.answerLevel2:
        print(Levels.Level2.Level2success)
        Level = 3
        ProgressTracker()
    elif Level == 3 and answer == Levels.Level3.Level3answer:
        print(Levels.Level3.Level3success)
        Level = 4
        ProgressTracker()
    elif answer == "hint":
        hint()
    elif Level == 4 and answer == "again":
        Level = 1
        ProgressTracker()
    elif Level == 4 and answer == "stop":
        Level = 0
        StartCheck()
    
    else:
        print("""
              Hmm. Leider falsch... Falls du einen Tipp willst gib (hint) ein!
              """)
        return Abfrage()
    
def hint():
    if Level == 1:
        print("Hauptstadt Amerikas")
    if Level == 2:
        print("Marinen...")
    if Level == 3:
        print("Für diese Frage gibt es leider keinen Tipp ;)")
    return Abfrage()

def ProgressTracker():
    if Level == 1:
        print(LevelEins)
        Abfrage()
    elif Level == 2:
        print(LevelZwei)
        Abfrage()
    elif Level == 3:
        print(LevelDrei)
        Abfrage()
    elif Level == 4:
        print(Levels.Erfolg)
        Abfrage()
    

def Quit():
    if answer == "quit":
        exit()
    else:
        checkAnswer()

def win():
    print(Levels.Erfolg)

# Spielloop
StartCheck()
Abfrage()


# Wer den Code klaut ist ein schlechter Mensch ;)
