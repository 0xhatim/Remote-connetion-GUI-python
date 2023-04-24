import socket
import threading
import time

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.connected_ips = {}

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5) # Queue 5 
        print(f"Server listening on {self.ip}:{self.port}")

        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()

    def accept_connections(self):
        while True:
            self.client_socket , address = self.server_socket.accept() # address for ip 
            print(f"Connection established from {address}")
            self.connected_ips[len(self.connected_ips)+1] = address[0]

    def send_all(self, message):
        if self.client_socket:
            self.client_socket.sendall(bytes(message, "utf-8"))
            print(f"Sent message: {message}")
            response = self.client_socket.recv(1024).decode()
            print(f"Response: {response}")
        else:
            print("No client connected.")
    def send_message(self, message, ip):
        if self.client_socket:
            self.client_socket.sendto(bytes(message, "utf-8"), (ip, self.port))
            print(f"Sent message: {message} to {ip}")
            response = self.client_socket.recv(1024).decode()
            print(f"Response: {response}")
        else:
            print("No client connected.")
if __name__ == "__main__":
    # Create and start server
    server = Server("192.168.0.153", 9016)
    server.start()
    
    # Keep connection alive until manually closed
    while True:
        print("Connected IPs: ", server.connected_ips)
        cmd = input("Command ")
        server.send_all(cmd)

