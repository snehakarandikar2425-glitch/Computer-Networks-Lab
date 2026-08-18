import socket

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP address and port
server_socket.bind(("localhost", 12345))

# Listen for client connection
server_socket.listen(1)

print("Server is waiting for connection...")

# Accept client connection
client_socket, address = server_socket.accept()

print("Connected to:", address)

# Receive message
message = client_socket.recv(1024).decode()

print("Message from client:", message)

# Send response
client_socket.send("Message received by server.".encode())

# Close connections
client_socket.close()
server_socket.close()
