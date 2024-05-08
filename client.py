import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Connection to hostname on the port.
client_socket.connect((host, port))

# Send a message
message = 'Hello, server!'
client_socket.send(message.encode())

# Receive no more than 1024 bytes
data = client_socket.recv(1024)

print(f"Received from server: {data.decode()}")

# Close the connection
client_socket.close()
