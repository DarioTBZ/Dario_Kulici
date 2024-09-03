import socket
import threading

SERVER = "10.20.1.59"
PORT = 55555
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("What is your nickname?\n")


def login():
    print("Do you want to login to a server? [y, n]")
    exit = input()
    if exit == "n":
        return 1
    else:
        client.connect((SERVER, int(PORT)))
        return 0

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "NICK":
                client.send(nickname.encode(FORMAT))
            elif message == "!quit":
                break
            else:
                print(message)
        except:
            print("You successfully exited the server...")
            client.close()
            break

def write():
    while True:
        text = input()
        match text:
            case "!quit":
                client.send("!quit".encode(FORMAT))
                client.close()
                break
            case "!help":
                client.send("!help".encode(FORMAT))
            case _:
                message = f"{nickname}: {text}"
                client.send(message.encode(FORMAT))

if login() > 0:
    print("Quitting...")
else:
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()