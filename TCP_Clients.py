import socket

#cs = client server
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 9999
#client connects to server
cs.connect((host, port))

#declare variable to store client's name
name = input('Kindly fill in your name')
#Client's name is sent to server
cs.send(bytes(name, 'utf-8'))

#message received from server by clients in TCP packets
message = cs.recv(1024).decode()
print(message)
#close connection
cs.close()

