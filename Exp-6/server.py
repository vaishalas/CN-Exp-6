import socket
import threading

# Server settings
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
UDP_PORT = 5001
BUFFER_SIZE = 1024

# Lists to manage connected TCP clients
tcp_clients = []

# TCP server setup
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((TCP_IP, TCP_PORT))
tcp_server.listen()

# UDP server setup
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((TCP_IP, UDP_PORT))

# Broadcast a message to all TCP clients
def broadcast_tcp(message, exclude_client=None):
    for client in tcp_clients:
        if client != exclude_client:
            try:
                client.send(message)
            except:
                tcp_clients.remove(client)

# Handle individual TCP client messages
def handle_tcp_client(client_socket):
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE)
            if message:
                broadcast_tcp(message, exclude_client=client_socket)
            else:
                break
        except:
            break
    client_socket.close()
    tcp_clients.remove(client_socket)

# Listen for TCP connections
def tcp_connection_listener():
    print(f"TCP server listening on {TCP_IP}:{TCP_PORT}")
    while True:
        client_socket, _ = tcp_server.accept()
        tcp_clients.append(client_socket)
        thread = threading.Thread(target=handle_tcp_client, args=(client_socket,))
        thread.start()

# Listen for UDP messages and broadcast them
def udp_message_listener():
    print(f"UDP server listening on {TCP_IP}:{UDP_PORT}")
    while True:
        message, addr = udp_server.recvfrom(BUFFER_SIZE)
        for client in tcp_clients:
            client.send(b"UDP:" + message)  # Prefix for clarity on receiving side

# Start TCP and UDP listeners
tcp_listener_thread = threading.Thread(target=tcp_connection_listener)
udp_listener_thread = threading.Thread(target=udp_message_listener)

tcp_listener_thread.start()
udp_listener_thread.start()
