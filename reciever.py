import socket
import random
import os

# Clear the screen (platform-specific command)
os.system('cls' if os.name == 'nt' else 'clear')

# Client configuration
server_ip = '192.168.1.0'  # Loopback address for local testing
server_port = 2718
random.seed(123)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout of 30 seconds
client_socket.settimeout(60)

try:
    # Connect to the server
    print("Waiting for server.....")
    client_socket.connect((server_ip, server_port))
    print("Connected to {}:{}".format(server_ip, server_port))
    print("")
    # Receive packets one by one and reconstruct the message
    received_packets = {}
    while True:
        packet = client_socket.recv(1024).decode()
        if not packet:
            break
        packet_number, packet_data = packet.split(':', 1)
        received_packets[int(packet_number)] = packet_data
        print("Received packet: {}".format(packet))
    print("")
    # Sort packets based on packet numbers from 0 to 5
    sorted_packets = [received_packets[i] for i in range(6) if i in received_packets]

    # Reconstruct the original message from received packets
    reconstructed_message = ''.join([received_packets[key] for key in sorted(received_packets.keys())])
    print("Reconstructed Message: {}".format(reconstructed_message))
    print("")

except socket.timeout:
    print("Error: Connection or data reception took too long")

finally:
    client_socket.close()