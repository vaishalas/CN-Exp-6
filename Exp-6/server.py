import threading
import socket

# UDP server should use SOCK_DGRAM (not SOCK_STREAM)
def udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Using SOCK_DGRAM for UDP
    udp_socket.bind(('localhost', 12346))  # Using port 12346 for UDP
    print(f"UDP Server Started at Port 12346")

    while True:
        message, client_address = udp_socket.recvfrom(1024)
        print(f"Received Message from {client_address} Message: {message.decode('utf-8')}")

# TCP server should use SOCK_STREAM
def tcp_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('localhost', 12345))  # Using port 12345 for TCP
    tcp_socket.listen(5)
    print(f"TCP Server Started at Port 12345")
    client_socket, client_address = tcp_socket.accept()
    print(f"Client Joined From {client_address}")
    handle_tcp_client(client_socket)

def handle_tcp_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f'Received Message: {message}')
        client_socket.send("Message Received".encode('utf-8'))
    client_socket.close()

# Function to start the correct server based on input
def start_server(name):
    if name.lower() == 'udp':
        threading.Thread(target=udp_server).start()
    elif name.lower() == 'tcp':
        threading.Thread(target=tcp_server).start()
    else:
        print("Invalid protocol choice. Please enter either 'TCP' or 'UDP'.")

if __name__ == '__main__':
    name = input("Enter TCP/UDP Connection needed: ")
    start_server(name)
