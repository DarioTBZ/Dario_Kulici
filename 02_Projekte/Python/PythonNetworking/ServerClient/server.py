import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55555 # Has to be an unused port
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat.".encode(FORMAT))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        # Get nickname from client
        client.send("NICK".encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode(FORMAT))
        client.send("Connected to the server!".encode(FORMAT))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()



print(f"""
    ------------------------------------
    Server:
    
    IP: {SERVER}
    Port: {PORT}
      
    Server is online and listening...
    ------------------------------------
      """)
receive()