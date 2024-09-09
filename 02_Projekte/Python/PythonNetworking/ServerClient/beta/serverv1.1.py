import socket, threading, datetime, time

SERVER = "127.0.0.1"
PORT = 54155
FORMAT = "utf-8"

# System commands
SYS_QUIT = "!quit"
SYS_HELP = "!help"

# Decide if server should run on localhost or ip address in network
def deployment():
    choose_deployment = ""
    while choose_deployment not in ["l", "n"]:
        print("Do you want to deploy the server on localhost or network? [l, n]")
        choose_deployment = input()
    return choose_deployment

choose_deployment = deployment()

if choose_deployment == "l":
    SERVER = "127.0.0.1"
elif choose_deployment == "n":
    HOST_IP = socket.gethostbyname(socket.gethostname())
    SERVER = HOST_IP

ADDR = (SERVER, PORT)

# Create socket and set server to listen for incoming connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
server_running = True

clients = []
nicknames = []

def server_terminal():
    while True:
        command = input()
        match command:
            case "kill":
                server_running = False
                server.close()
                return 1
            case _:
                pass

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            client.send(message)


def break_connection(client, addr):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    broadcast(f"{nickname} left the chat.".encode(FORMAT), client)
    print(f"Disconnected from {addr}, ({nickname}).")
    nicknames.remove(nickname)

def check_msg(msg, client):
    match msg.decode(FORMAT):
        case "!quit": # replace manually if changing SYS constants
            client.send(SYS_QUIT.encode(FORMAT))
            break_connection(client)
            return 1
        case "!help": # replace manually if changing SYS constants
            client.send(f"""------------------------------------
                        
Available commands: 
                        
    {SYS_QUIT} - Quits the server.
    {SYS_HELP} - Prints this menu
                        
Type in the chat to communicate with others. 
        
------------------------------------
                        """.encode(FORMAT))
        case _:
            return 0
    

def handle_client(client, addr):
    while True:
        if server_running == False:
            break
        try:
            message = client.recv(1024)
            match check_msg(message, client):
                case 1: # = client quits server
                    break

            broadcast(message, client)
        except:
            break_connection(client, addr)
            break

def receive():
    while True:
        if server_running == False:
            break

        client, addr = server.accept()
        print(f"Connected with {str(addr)}.")

        # Get nickname from client
        client.send("NICK".encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode(FORMAT), client)
        client.send("Connected to the server! Type !help to see a list of commands".encode(FORMAT))

        thread = threading.Thread(target=handle_client, args=(client, addr,))
        thread.start()

        


def process_timer():
    while True:
        if server_running == False:
            break

        now = datetime.datetime.now()
        print(now.strftime("%Y.%m.%d, %H:%M:"), " active threads: ", threading.active_count() - 1)
        time.sleep(60)
        

server_start = datetime.datetime.now()
print(f"""
    ------------------------------------
    Server started at {server_start.strftime("%H:%M:%S")}:
    
    IP: {SERVER}
    Port: {PORT}
      
    Server is online and listening...
    ------------------------------------
      """)

process_thread = threading.Thread(target=process_timer)
process_thread.start()

server_terminal = threading.Thread(target=server_terminal)
server_terminal.start()

receive()