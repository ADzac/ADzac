import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
print(host)
port = 65432
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
connection,address = ServerSideSocket.accept()
#def multi_threaded_client(connection):
connection.send(str.encode('Server is working:'))
command  = input(str("Command :"))
connection.send(command.encode())
data = connection.recv(2048)
if data:
	print('PC Tutup')
ServerSideSocket.close()
