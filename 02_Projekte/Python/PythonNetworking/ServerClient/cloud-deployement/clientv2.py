import socket
import threading
import json

nickname = input("Choose your nickname: ")
master_ip = input("Master Server IP Address: ")
master_port = 6000

# Connect to Master Server
master_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_client.connect((master_ip, master_port))

# Request Chatroom Server Connection
request = json.dumps({"action": "connect_to_chatroom"})
master_client.send(request.encode('utf-8'))

response = json.loads(master_client.recv(1024).decode('utf-8'))
if response.get("status") == "ok":
    ipaddress = response["server_ip"]
    port = response["server_port"]
    print(f"Connecting to chatroom server at {ipaddress}:{port}")
    master_client.close()
else:
    print("Error:", response.get("message"))
    master_client.close()
    exit(1)

# Connect to Chatroom Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipaddress, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        if message.split(": ")[1] == "!quit":
            client.send("!quit".encode('utf-8'))
            client.close()
            break
        elif message.split(": ")[1] == "!help":
            client.send("!help".encode('utf-8'))
        else:
            client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
