import socket

HOST = 'localhost'  # Server IP address
PORT = 9014  # Server port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)

# A list to hold the connected IPs
connected_ips = []

# Wait for incoming connections
counter = 0
while True:
    # Establish a connection with a client
    client_socket, addr = server_socket.accept()

    # Add the IP address to the list of connected IPs
    connected_ips.append(addr[0])

    # Print the list of connected IPs
    print("Connected IPs:", connected_ips)

    # Close the connection
    client_socket.close()