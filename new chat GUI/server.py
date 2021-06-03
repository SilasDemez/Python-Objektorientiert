import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 7976
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

print("Hosting on: " + HOST + ", " + str(PORT))


# broadcast
def broadcast(message):
    for client in clients:
        client.send(message)


# receive
def receive():
    while True:
        client, address = server.accept()
        print("Connected with " + str(address))

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print("Nickname of the client is: " + str(nickname))
        broadcast(nickname + " connected to the server!\n".encode(FORMAT))
        client.send("Connected to the server".encode(FORMAT))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# handle
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}says {message}")
            broadcast(message)
        except:
            index = clients.index(clients)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)


receive()
