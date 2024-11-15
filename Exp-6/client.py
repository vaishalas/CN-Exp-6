import threading
import socket

def tcp_client():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.connect(('localhost',12345))
    while True:
        message = input("Enter The message or Type Bye: ")
        if message.lower() == 'bye':
            break
        else:
            tcp_socket.send(message.encode('utf-8'))
            responce = tcp_socket.recv(1024).decode('utf-8')
            print(f'Responce From Server {responce}')

    tcp_socket.close()

def udp_client():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.connect(('localhost',12346))

    while True:
        message = input("Enter The message or Type Bye: ")
        if message.lower() == 'bye':
            break
        else:
            udp_socket.send(message.encode('utf-8'))
def start_client(name):
    if name == 'udp':
        threading.Thread(target=udp_client).start()
    else:
        threading.Thread(target=tcp_client).start()

if __name__ == '__main__':
    name = input("Enter The connection name(TCP/UDP): ")
    start_client(name.lower())
