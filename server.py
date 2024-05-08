import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Start listening for clients
server_socket.listen(5)

print("Server listening...")

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    
    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received '{data.decode()}' from the client")

    # Send data back as an echo
    client_socket.send(data)

    # Close the connection with the client
    client_socket.close()
    print("Connection closed")
    break  # This breaks after one connection for simplicity
