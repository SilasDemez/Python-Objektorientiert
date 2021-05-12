# coding=utf-8
import socket, threading

host = '127.0.0.1'  # LocalHost
port = 7976  # Port wählen

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket initialisieren
server.bind((host, port))  # binding host und port zu einem socket
server.listen()

clients = []
nicknames = []


def broadcast(message):  # broadcast funktion
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:  # recieving messages vom Client
            message = client.recv(1024)
            broadcast(message)
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


receive()
