import socket
import threading
import redis
import json
import time
import requests

def get_public_ip():
    try:
        token = requests.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
        ).text

        public_ip = requests.get(
            "http://169.254.169.254/latest/meta-data/public-ipv4",
            headers={"X-aws-ec2-metadata-token": token}
        ).text

        return public_ip

    except requests.RequestException as e:
        print(f"Error retrieving public IP: {e}")
        exit(1)

def get_network_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

clients = []
nicknames = []
client_lock = threading.Lock()
HOST_IP = get_network_ip()
CHATROOM_PORT = 5555
PUBLIC_IP = get_public_ip()

master_ip = '10.0.1.143'
master_port = 6000

try:
    redis_client = redis.StrictRedis(host=HOST_IP, port=6379, decode_responses=True)
    redis_client.ping()
except redis.exceptions.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")
    exit(1)

pubsub = redis_client.pubsub()
pubsub.subscribe("chatroom")

def register_with_master():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as master_socket:
            master_socket.connect((master_ip, master_port))
            registration_message = json.dumps({
                "action": "heartbeat",
                "server_ip": HOST_IP,
                "server_port": CHATROOM_PORT
            })
            master_socket.send(registration_message.encode('utf-8'))
            response = json.loads(master_socket.recv(1024).decode('utf-8'))
            if response.get("status") == "ok":
                print("Successfully registered with Master Server.")
            else:
                print("Registration failed:", response.get("message"))
    except Exception as e:
        print(f"Error registering with Master Server: {e}")

def send_heartbeat():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as heartbeat_socket:
                heartbeat_socket.connect((master_ip, master_port))
                heartbeat_message = json.dumps({
                    "action": "heartbeat",
                    "server_ip": PUBLIC_IP,
                    "server_port": CHATROOM_PORT
                })
                heartbeat_socket.send(heartbeat_message.encode('utf-8'))
                response = json.loads(heartbeat_socket.recv(1024).decode('utf-8'))
                if response.get("status") != "ok":
                    print("Heartbeat failed:", response.get("message"))
                time.sleep(10)
        except Exception as e:
            print(f"Error sending heartbeat: {e}")
            time.sleep(10)

def broadcast(message):
    try:
        redis_client.publish("chatroom", message)
    except redis.exceptions.ConnectionError as e:
        print(f"Error while broadcasting message: {e}")

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "!quit":
                with client_lock:
                    index = clients.index(client)
                    nickname = nicknames[index]
                    broadcast(f"{nickname} has left the chat!")
                    clients.remove(client)
                    nicknames.remove(nickname)
                    client.close()
                break
            elif message == "!help":
                client.send("Commands:\n!quit - Leave the chat\n!help - Show this help message".encode('utf-8'))
            elif message == "!ip":
                client.send(f"Puglic IP: {PUBLIC_IP}, Private IP: {HOST_IP}")
            else:
                broadcast(message)
        except Exception as e:
            print(f"Error handling client: {e}")
            with client_lock:
                if client in clients:
                    index = clients.index(client)
                    clients.remove(client)
                    client.close()
                    nickname = nicknames[index]
                    broadcast(f"{nickname} has left the chat!")
                    nicknames.remove(nickname)
            break

def handle_redis_messages():
    for message in pubsub.listen():
        if message['type'] == 'message':
            broadcast_message = message['data']
            with client_lock:
                for client in clients:
                    client.send(broadcast_message.encode('utf-8'))

def receive():
    while True:
        client, address = server.accept()
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        with client_lock:
            nicknames.append(nickname)
            clients.append(client)
        broadcast(f"{nickname} joined the chat!")
        client.send("Connected to the server.".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST_IP, CHATROOM_PORT))
server.listen()

print("Chatroom Server is running...")

register_with_master()

heartbeat_thread = threading.Thread(target=send_heartbeat)
heartbeat_thread.start()

redis_thread = threading.Thread(target=handle_redis_messages)
redis_thread.start()

receive()
