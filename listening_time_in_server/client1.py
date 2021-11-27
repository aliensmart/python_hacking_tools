import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

client_socket.connect((host, port))

tm = client_socket.recv(1024)
client_socket.close()

print('the time got is %s' % tm.decode('ascii'))

