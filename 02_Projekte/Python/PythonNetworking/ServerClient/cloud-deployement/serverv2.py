import socket
import threading
import redis

clients = []
nicknames = []

client_lock = threading.Lock()
HOST_IP = socket.gethostbyname(socket.gethostname())

try:
    redis_client = redis.StrictRedis(host=HOST_IP, port=6379, decode_responses=True)
    redis_client.ping()
except redis.exceptions.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")
    exit(1)

pubsub = redis_client.pubsub()
pubsub.subscribe("chatroom")

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
            else:
                broadcast(message)
        except Exception as e:
            print(f"Error handling client: {e}")
            with client_lock:
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
server.bind(('0.0.0.0', 5555))
server.listen()

print("Server is running...")

redis_thread = threading.Thread(target=handle_redis_messages)
redis_thread.start()
receive()