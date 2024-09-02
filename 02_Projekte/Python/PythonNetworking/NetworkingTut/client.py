import socket

HEADER = 64
SERVER = "10.20.1.53"
PORT = 55555
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!quit"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def chat():
    connection = True

    while connection:
        message = input()
        if message == DISCONNECT_MESSAGE:
            break
        else:
            send(message)

chat()
send(DISCONNECT_MESSAGE)
print("Disconnected from the server...")