import socket 
import sys

# Creating a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
s.connect(server_address)

try:
    # Send Data
    message = b'This is the message. It will be repeated.'
    print('Sending {!r}'.format(message))
    s.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = s.recv(16)
        amount_received += len(data)
        print('Received {!r}'.format(data))
        
finally:
    print('closing socket')
    s.close()
    