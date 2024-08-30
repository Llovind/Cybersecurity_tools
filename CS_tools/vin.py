import socket
import os
import platform

def tcp_client(targetHost, targetPort, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((targetHost, targetPort))

    # Mengirim permintaan HTTP GET ke target host
    client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

    # Menerima respons dari server
    response = client.recv(4096)
    print(response.decode())

    client.close()

def udp_client(server_ip, server_port, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(message.encode(), (server_ip, server_port))

    response, _ = client.recvfrom(4096)
    print(f"Received from UDP Server: {response.decode()}")

    client.close()

def ping_host(targetHost):
    # Tentukan perintah ping berdasarkan sistem operasi
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Jalankan perintah ping
    command = f"ping {param} 4 {targetHost}"
    response = os.system(command)

    if response == 0:
        print(f"{targetHost} is up!")
    else:
        print(f"{targetHost} is down!")


def main_menu():
    while True:
        print("Welcome To T'vin")
        print("Select an option:")
        print("1. TCP Client")
        print("2. UDP Client")
        print("3. Ping Host")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            targetHost = input("Enter the server host (hostname or IP): ")
            targetPort = int(input("Enter the server port: "))
            message = "GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n"
            tcp_client(targetHost, targetPort, message)
        elif choice == '2':
            server_ip = input("Enter the server IP: ")
            server_port = int(input("Enter the server port: "))
            message = input("Enter the message to send: ")
            udp_client(server_ip, server_port, message)
        elif choice == '3':
            targetHost = input("Enter the host to ping: ")
            ping_host(targetHost)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()
