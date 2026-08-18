import socket

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("localhost", 12345))

# Get message from user
message = input("Enter message: ")

# Send message to server
client_socket.send(message.encode())

# Receive response
response = client_socket.recv(1024).decode()

print("Server response:", response)

# Close connection
client_socket.close()
