import socket, threading, datetime, time
# socket.gethostbyname(socket.gethostname())
SERVER = "192.168.1.116"
PORT = 54155 # Has to be an unused port
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
#now = datetime.now()

# System commands
SYS_QUIT = "!quit"
SYS_HELP = "!help"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

clients = []
nicknames = []

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



#def process_timer():
 #   while True:
  #      time.sleep(5)
   #     print(now.strftime("%d.%m.%Y %H.%M"), " active threads: ", threading.active_count() - 1)



print(f"""
    ------------------------------------
    Server:
    
    IP: {SERVER}
    Port: {PORT}
      
    Server is online and listening...
    ------------------------------------
      """)
#process_thread = threading.Thread(target=process_timer)
#process_thread.start()

receive()

