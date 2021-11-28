import socket 
import sys 

# Creating a TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print("Starting up on {} port {}".format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
            
        # Receive data in small chunks and retransmit it
        while True:
            #we receive the client data and 
            data = connection.recv(16)
            # and print the client data
            print('received {!r}'.format(data))
            if data:
                print("Sending data back to the client")
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()
        
