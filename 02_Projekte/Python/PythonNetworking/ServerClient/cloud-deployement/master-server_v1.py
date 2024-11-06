import socket
import threading
import json
import time
import random

def get_network_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

master_host = get_network_ip()
master_port = 6000
chatroom_servers = {}

def handle_heartbeat(server_ip, server_port):
    chatroom_servers[(server_ip, server_port)] = time.time()
    print(f"Received heartbeat from Chatroom Server at {server_ip}:{server_port}")

def remove_stale_servers():
    while True:
        time.sleep(10)
        current_time = time.time()
        for server, last_heartbeat in list(chatroom_servers.items()):
            if current_time - last_heartbeat > 15:
                del chatroom_servers[server]
                print(f"Removed stale Chatroom Server: {server[0]}:{server[1]}")

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            request = json.loads(data)

            if request.get("action") == "connect_to_chatroom":
                if chatroom_servers:
                    chatroom_server = random.choice(list(chatroom_servers.keys()))
                    response = {
                        "status": "ok",
                        "server_ip": chatroom_server[0],
                        "server_port": chatroom_server[1]
                    }
                else:
                    response = {"status": "error", "message": "No available chatroom servers"}

            elif request.get("action") == "heartbeat":
                server_ip = request.get("server_ip")
                server_port = request.get("server_port")
                handle_heartbeat(server_ip, server_port)
                response = {"status": "ok"}

            else:
                response = {"status": "error", "message": "Invalid action"}

            client_socket.send(json.dumps(response).encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {e}")
            break
    client_socket.close()

def start_master_server():
    master_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_server.bind((master_host, master_port))
    master_server.listen()
    print(f"Master Server is running on {master_host} on Port {master_port}")
    print("Listening for connections...\n")

    stale_remover_thread = threading.Thread(target=remove_stale_servers)
    stale_remover_thread.start()

    while True:
        client_socket, client_address = master_server.accept()
        print(f"Connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

start_master_server()
