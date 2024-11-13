import socket
import threading

# Server settings
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
UDP_PORT = 5001
BUFFER_SIZE = 1024

# Setup TCP client
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((TCP_IP, TCP_PORT))

# Setup UDP client
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Receive messages from TCP server
def receive_tcp_messages():
    while True:
        try:
            message = tcp_client.recv(BUFFER_SIZE)
            if message:
                print(message.decode())
        except:
            break

# Send message over TCP
def send_tcp_message(message):
    tcp_client.send(message.encode())

# Send message over UDP
def send_udp_message(message):
    udp_client.sendto(message.encode(), (TCP_IP, UDP_PORT))

# Start a thread to listen for TCP messages
tcp_thread = threading.Thread(target=receive_tcp_messages)
tcp_thread.start()

# Example usage
while True:
    msg = input("Enter message (type 'udp:' prefix for UDP message): ")
    if msg.startswith('udp:'):
        send_udp_message(msg[4:])
    else:
        send_tcp_message(msg)
