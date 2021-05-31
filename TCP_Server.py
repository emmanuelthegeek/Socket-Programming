#import socket  and datetime modules
import socket
from datetime import datetime

#declare variables for IP address(IPv4), and port number
host = 'localhost'
port = 9999

#ss = server side
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Check if server was created
print('server created successfully')

ss.bind((host, port))
#wait for connection from clients
ss.listen(3)
#Check if connection is created
print('waiting for connections.......')

while True:
    cs, addr = ss.accept()
    #log time connected
    time = datetime.now()
    #Receive name of client
    name = cs.recv(1024).decode()
    print(f'{name} connected with{addr} on {time}')
    #Message is sent to clients
    cs.send(bytes(f'You are welcome dear {name}, how may we be of help?', 'utf-8'))
    #connection closed
    cs.close()

