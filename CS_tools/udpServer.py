import socket

localIP = "127.0.0.1"
localPort = 9997
buffer = 1024

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((localIP, localPort))

print("Server Up")

while(True):
    data = serverSocket.recvfrom(buffer)
    pesan = data[0]
    ip_addr = data[1]
    print("Pesan dari client: \"{}\"".format(pesan))
    print("IP client: \"{}\"".format(ip_addr))

    serverSocket.sendto(b"Selamat datang di UDP server", ip_addr)
