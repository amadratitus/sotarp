# sotarp
simulation of transmit and receive process using python
<p>
In data communication, a message can be sent from one location to a remote computer in a
different network in the same country or internationally. The route followed may not be the same
for the whole message to reach the destination.
What happens is that a message may be broken into packets, and each packet is given a number.
These packets may follow different routes to the destination. When the packets are received, the
whole message is reconstructed.
What you are required to do is:
Develop and implement a simulation of transmit and receive process using C/C++
programming language or any language of your convenience that you can explain fully.
Prompt a person to indicate the file which contains the text information to send. Read the
information and break it into chunks of 5 characters each which will constitute a packet. Give it a
number and display it on the screen. Send the message in an unordered sequence. After the
whole message has been sent then try to receive these packets one by one and then later display
the whole message. The receiving computer may be any other computer on the network
</p>

<h4>
transmitter.py
</h4>

```
import socket
import random
import os

# Clear the screen (platform-specific command)
os.system('cls' if os.name == 'nt' else 'clear')
# Server configuration
server_ip = '127.0.0.1' 
server_port = 2718
# random.seed(123)

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

```
<br>
<h4>
reciever.py
</h4>

```
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

```
