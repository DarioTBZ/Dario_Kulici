import socket
import threading

SERVER = "10.20.1.53"
PORT = 55555
FORMAT = "utf-8"

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "NICK":
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error ocurred")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input("")}"
        client.send(message.encode(FORMAT))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()