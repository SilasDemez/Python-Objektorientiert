# coding=utf-8
import socket, threading

host = '127.0.0.1'  # LocalHost
port = 7976  # Port wählen

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket initialisieren
server.bind((host, port))  # binding host und port zu einem socket
server.listen()

clients = []
nicknames = []


# function to start the connection
def startChat():
    print("server is working on " + host)

    # listening for connections
    server.listen()

    while True:
        # accept connections and returns
        # a new connection to the client
        #  and  the address bound to it
        conn, addr = server.accept()
        # conn.send("NAME".encode("utf8"))

        # 1024 represents the max amount
        # of data that can be received (bytes)
        # name = conn.recv(1024).decode("utf8")

        # append the name and client
        # to the respective list
        # nicknames.append(name)
        clients.append(conn)

        # print(f"Name is :{name}")

        # broadcast message
        # broadcastMessage(f"{name} has joined the chat!".encode("utf8"))

        conn.send('Connection successful!'.encode("utf8"))

        # Start the handling thread
        thread = threading.Thread(target=handle,
                                  args=(conn, addr))
        thread.start()

        # no. of clients connected
        # to the server
        print(f"active connections {threading.activeCount() - 1}")


# method to handle the
# incoming messages
def handle(conn, addr):
    print("WTF")
    # print(f"new connection {addr}")

    connected = True

    # str = username + " joined the chat!"
    # broadcastMessage(str)
    # print(username + " joined the chat!")


    while connected:
        # recieve message
        print("Waiting for message")
        message = conn.recv(1024)

        print(message)

        # broadcast message
        broadcastMessage(message.encode("utf-8"))

    # close the connection
    conn.close()


# method for broadcasting
# messages to the each clients
def broadcastMessage(message):
    for client in clients:
        client.send(message)


# call the method to
# begin the communication
startChat()


def broadcast(message):  # broadcast funktion
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:  # recieving messages vom Client
            message = client.recv(1024)
            print(message)
            broadcast(message)
            print("Mesage: " + message)
        except:  # löschen der Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} hat verlassen!'.format(nickname).encode('utf8'))
            nicknames.remove(nickname)
            break


def receive():  # mehrere Clients empfangen
    while True:

        while True:
            """Accepts a connection request and stores two parameters, 
            conn which is a socket object for that user, and addr 
            which contains the IP address of the client that just 
            connected"""
            conn, addr = server.accept()

            """Maintains a list of clients for ease of broadcasting 
            a message to all available people in the chatroom"""
            list_of_clients.append(conn)

            # prints the address of the user that just connected
            # print(addr[0] + " connected")

            # creates and individual thread for every user
            # that connects
            start_new_thread(clientthread, (conn, addr))

        conn.close()
        server.close()

        client, address = server.accept()
        print("Verbunden mit {}".format(str(address)))
        client.send('Nickname eingeben:'.encode('utf8'))
        nickname = client.recv(1024).decode('utf8')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('utf8'))
        client.send('Connected to server!'.encode('utf8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()




