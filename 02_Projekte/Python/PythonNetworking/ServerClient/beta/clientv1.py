import socket
import threading

SERVER = "192.168.1.116"
PORT = 54155
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("What is your nickname?\n")


def login():
    print("Do you want to login to a server? [y, n]")
    exit = input()
    if exit == "n":
        return 1
    else:
        SERVER = input("IP (bsp. 10.10.1.1): ")
        if SERVER == "":
            SERVER = "10.20.101.62"
        try:
            client.connect((SERVER, int(PORT)))
        except:
            print("No Server was found under this ip address.")
            return 1
        return 0

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            match message:
                case "NICK":
                    client.send(nickname.encode(FORMAT))
                case "!quit":
                    break
                case "rps":
                    print("Joined Rock Paper Scissors Game.")

                case _:
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
                try:
                    message = f"{nickname}: {text}"
                    client.send(message.encode(FORMAT))
                except:
                    print("test")

if login() > 0:
    print("Connection closed")
else:
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()