import socket
import threading
import time
import datetime

FORMAT = "utf-8"
BROADCAST_PORT = 54156  # Port für die Serversuche
BUFFER_SIZE = 1024

# Server-Setup
SERVER_BASE = "127.0.0."  # Basis für Loopback-IPs
server_index = None  # Benutzerdefinierte IP-Index

server_running = threading.Event()
server_running.set()

clients = []
nicknames = []
server_sockets = []  # TCP-Verbindungen zu anderen Servern

def server_terminal():
    """Verarbeitet Terminal-Eingaben zur Serversteuerung."""
    while server_running.is_set():
        command = input()
        if command == "kill":
            server_running.clear()
            print("Server wird heruntergefahren...")
            break

def broadcast_message(message, sender_client=None):
    """Sendet die Nachricht an alle Clients und Server."""
    # Nachricht an alle Clients senden
    for client in clients:
        if client != sender_client:
            client.send(message)

    # Nachricht an alle verbundenen Server senden
    for server_sock in server_sockets:
        try:
            server_sock.send(message)
        except:
            server_sockets.remove(server_sock)

def break_connection(client, addr):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        broadcast_message(f"{nickname} left the chat.".encode(FORMAT), client)
        print(f"Disconnected from {addr}, ({nickname}).")
        nicknames.remove(nickname)

def check_msg(msg, client):
    match msg.decode(FORMAT):
        case "!quit":
            client.send("!quit".encode(FORMAT))
            break_connection(client, addr=None)
            return 1
        case "!help":
            client.send(f"""Available commands:\n
                          !quit - Quits the server.\n
                          !help - Prints this menu.\n""".encode(FORMAT))
        case _:
            return 0

def handle_client(client, addr):
    while server_running.is_set():
        try:
            message = client.recv(BUFFER_SIZE)
            if check_msg(message, client) == 1:
                break
            # Broadcast message to all clients and other servers
            broadcast_message(message, client)
        except:
            break_connection(client, addr)
            break

def receive_clients():
    while server_running.is_set():
        try:
            client, addr = server.accept()
            print(f"Connected with {str(addr)}.")

            client.send("NICK".encode(FORMAT))
            nickname = client.recv(BUFFER_SIZE).decode(FORMAT)
            nicknames.append(nickname)
            clients.append(client)

            print(f"Nickname of the client is {nickname}")
            broadcast_message(f"{nickname} joined the chat!".encode(FORMAT), client)
            client.send("Connected to the server! Type !help to see a list of commands".encode(FORMAT))

            thread = threading.Thread(target=handle_client, args=(client, addr,))
            thread.start()
        except:
            break  # Verlasse Schleife, wenn `server.close()` ausgeführt wird

def server_broadcast():
    """Sendet regelmäßig UDP-Broadcasts zur Serversuche."""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    message = f"SERVER_DISCOVERY:{SERVER_BASE}{server_index}:{ADDR[1]}".encode(FORMAT)
    
    while server_running.is_set():
        udp_socket.sendto(message, ('<broadcast>', BROADCAST_PORT))
        time.sleep(5)  # Alle 5 Sekunden einen Broadcast senden

def listen_for_servers():
    """Hört auf UDP-Broadcasts, um andere Server zu entdecken."""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((SERVER_BASE + str(server_index), BROADCAST_PORT))
    
    while server_running.is_set():
        try:
            message, address = udp_socket.recvfrom(BUFFER_SIZE)
            msg = message.decode(FORMAT)
            if msg.startswith("SERVER_DISCOVERY"):
                _, server_ip, server_port = msg.split(':')
                server_addr = (server_ip, int(server_port))
                if server_addr != ADDR and server_addr not in [sock.getpeername() for sock in server_sockets]:
                    connect_to_server(server_addr)
        except:
            break

def connect_to_server(server_addr):
    """Verbindet sich mit einem anderen Server."""
    try:
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.connect(server_addr)
        server_sockets.append(server_sock)
        print(f"Connected to server {server_addr}")
        threading.Thread(target=handle_server_messages, args=(server_sock,)).start()
    except Exception as e:
        print(f"Failed to connect to server {server_addr}: {e}")

def handle_server_messages(server_sock):
    while server_running.is_set():
        try:
            message = server_sock.recv(BUFFER_SIZE)
            if message:
                broadcast_message(message)  # Nachricht an alle Clients und Server weiterleiten
        except:
            server_sockets.remove(server_sock)
            server_sock.close()
            break

def process_timer():
    while server_running.is_set():
        now = datetime.datetime.now()
        print(now.strftime("%Y.%m.%d, %H:%M:%S:"), " active threads: ", threading.active_count() - 1)
        time.sleep(60)

# Benutzer nach der gewünschten IP-Adresse fragen
while True:
    try:
        server_index = int(input("Bitte geben Sie die IP-Adresse ein (z.B. 2 für 127.0.0.2): "))
        if 1 <= server_index <= 254:  # Erlaubt IPs von 127.0.0.1 bis 127.0.0.254
            break
        else:
            print("Bitte geben Sie eine gültige Zahl zwischen 1 und 254 ein.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

# Server-Setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_BASE + str(server_index), 0))  # 0 = zufälliger freier Port
ADDR = server.getsockname()  # Erhalte die tatsächliche Adresse (IP und Port)

server.listen()

print(f"""
    ------------------------------------
    Server started automatically:
    IP: {SERVER_BASE}{server_index}
    Port: {ADDR[1]}
    Server is online and listening...
    ------------------------------------
""")

# Threads starten
process_thread = threading.Thread(target=process_timer)
process_thread.start()

server_broadcast_thread = threading.Thread(target=server_broadcast)
server_broadcast_thread.start()

server_listener_thread = threading.Thread(target=listen_for_servers)
server_listener_thread.start()

server_terminal_thread = threading.Thread(target=server_terminal)
server_terminal_thread.start()

receive_clients()  # Starte das Empfangen von Clients
