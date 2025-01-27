import socket, threading, datetime, time

SERVER = "127.0.0.1"
PORT = 54155
FORMAT = "utf-8"

# System commands
SYS_QUIT = "!quit"
SYS_HELP = "!help"
SYS_GAME = "!rps"

def deployment():
    choose_deployment = ""
    while choose_deployment not in ["l", "n"]:
        print("Do you want to deploy the server on localhost or network? [l, n]")
        choose_deployment = input()
    return choose_deployment

# Deployment Auswahl ausführen
choose_deployment = deployment()
if choose_deployment == "l":
    SERVER = "127.0.0.1"
elif choose_deployment == "n":
    HOST_IP = socket.gethostbyname(socket.gethostname())
    SERVER = HOST_IP

ADDR = (SERVER, PORT)

server_running = threading.Event()
server_running.set()

clients = []
nicknames = []

def server_terminal():
    while True:
        command = input()
        if command == "kill":
            server_running.clear()  # Server beenden
            server.close()
            print("Server wird heruntergefahren...")
            break

def rps(client):
    client.send("rps".encode(FORMAT))
    print("Sent message")

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            client.send(message)

def break_connection(client, addr):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        broadcast(f"{nickname} left the chat.".encode(FORMAT), client)
        print(f"Disconnected from {addr}, ({nickname}).")
        nicknames.remove(nickname)

def check_msg(msg, client):
    match msg.decode(FORMAT):
        case "!quit":
            client.send(SYS_QUIT.encode(FORMAT))
            break_connection(client)
            return 1
        case "!help":
            client.send(f"""------------------------------------
Available commands: 
    {SYS_QUIT} - Quits the server.
    {SYS_HELP} - Prints this menu
Type in the chat to communicate with others. 
------------------------------------""".encode(FORMAT))
        case "!rsp":
            game_thread = threading.Thread(target=rps, args=(client,))
            game_thread.start()
        case _:
            return 0

def handle_client(client, addr):
    while server_running.is_set():
        try:
            message = client.recv(1024)
            if check_msg(message, client) == 1:
                break
            broadcast(message, client)
        except:
            break_connection(client, addr)
            break

def receive():
    while server_running.is_set():
        try:
            client, addr = server.accept()
            print(f"Connected with {str(addr)}.")

            client.send("NICK".encode(FORMAT))
            nickname = client.recv(1024).decode(FORMAT)
            nicknames.append(nickname)
            clients.append(client)

            print(f"Nickname of the client is {nickname}")
            broadcast(f"{nickname} joined the chat!".encode(FORMAT), client)
            client.send("Connected to the server! Type !help to see a list of commands".encode(FORMAT))

            thread = threading.Thread(target=handle_client, args=(client, addr,))
            thread.start()
        except:
            break  # Verlässt die Schleife, wenn `server.close()` ausgeführt wurde

def process_timer():
    while server_running.is_set():
        now = datetime.datetime.now()
        print(now.strftime("%Y.%m.%d, %H:%M:%S:"), " active threads: ", threading.active_count() - 1)
        time.sleep(60)

# Serverstart
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))
server.listen()

print(f"""
    ------------------------------------
    Server started:
    IP: {SERVER}
    Port: {PORT}
    Server is online and listening...
    ------------------------------------
""")

process_thread = threading.Thread(target=process_timer)
process_thread.start()

server_terminal_thread = threading.Thread(target=server_terminal)
server_terminal_thread.start()

receive()  # Beginne Verbindungen zu akzeptieren
