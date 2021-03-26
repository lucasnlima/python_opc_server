#socket_echo_client.py
import pywintypes
import socket
import sys
pywintypes.datetime = pywintypes.TimeType

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
get_ip_address

ip_gatway = "localhost"

#Interface Principal Client:
print("Client TCP/IP-OPC:")
print("\n Digite o IP do GATEWAY OPC: ")
ip_gatway = input()

if ip_gatway == "":
    ip_gatway = get_ip_address()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (ip_gatway, 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    


    while True:
        # Send message requiring arduino data
        message = b'Send data'
        sock.sendall(message)
        amount_received = 0
        # Look for the response
        data = sock.recv(100000)
        print('received:  {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()