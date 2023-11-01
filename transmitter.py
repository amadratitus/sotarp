import socket
import random
import os

# Clear the screen (platform-specific command)
os.system('cls' if os.name == 'nt' else 'clear')
# Server configuration
server_ip = '127.0.0.1' 
server_port = 2718
#random.seed(123)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((server_ip, server_port))

# Prompt the user to enter the file name containing text information
filename = input("Enter filename: ")
print("")

# Read the information from the file and break it into packets of 5 characters each
with open(filename, 'r') as file:
    message = file.read()
    packets = [(i // 5, message[i:i+5]) for i in range(0, len(message), 5)]

# Print the original unshuffled packets with numbers in 5-character chunks
for packet_number, packet_data in packets:
    print("Packet {}: {}".format(packet_number, packet_data))
print("")

# Shuffle the packets to send them in an unordered sequence
random.shuffle(packets)

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for the Client...")
print("Server listening on {}:{}".format(server_ip, server_port))
print("")

# Wait for a connection and send packets in an unordered sequence
client_socket, client_address = server_socket.accept()
print("Connection established with {}".format(client_address))
print("")

# Send packets in an unordered manner
for packet_number, packet_data in packets:
    packet = "{}:{}".format(packet_number, packet_data)
    client_socket.send(packet.encode())
    print("Sent packet: {}".format(packet))
print("")

client_socket.close()
server_socket.close()