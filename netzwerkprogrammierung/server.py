import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 49160))
#server_socket.bind(("127.69.69.69", 49160))
server_socket.listen(7)

while True:
    (client_socket, addr) = server_socket.accept()
    print("Incoming connection by", addr)
    byte_msg = client_socket.recv(1024)
    msg = str(byte_msg, "utf-8")
    print(msg)
# 49160
