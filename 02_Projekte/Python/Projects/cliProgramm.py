# databank for commands
class data:
    help = """Commandlist:
                    - help -- für Hilfe
                    - 
                 """
    
    
desktop = "desktop"
downloads = "downloads"
Directories = desktop, downloads


# functions
def inputmode():
    global answer
    answer = input("user$: ")
    checkcmd()

def checkcmd():
    if hasattr(data, answer):
        print(getattr(data, answer))
        return inputmode()
    if answer == "quit":
        exit()
        
    else:
        print(f"{answer}: Command not found")
        return inputmode()

        

def currentDirectory():
    global cd
    cd = desktop

# programm
inputmode()
