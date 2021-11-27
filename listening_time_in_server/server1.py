import socket 
import time

# Create a socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port =  9999

# bin the port 
serverSocket.bind((host, port))

# Queue up to 5 requests
serverSocket.listen(5)

while True:
    # Establisj connection
    # accept the connect and get the connected client address and socket
    clientsocket, addr = serverSocket.accept()
    print("Got a connection from %s " % str(addr))
    current_time = time.ctime(time.time()) + '\r\n'
    # send the current time to the client side
    clientsocket.send(current_time.encode('ascii'))
    clientsocket.close()
    
