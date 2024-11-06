import socket
import threading

nickname = input("Choose your nickname: ")
ipaddress = input("IP Address: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipaddress, 5555))

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
