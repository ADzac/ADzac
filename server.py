import socket
import os
from _thread import *


ServerSideSocket = socket.socket()
hostname = socket.gethostname()
host = socket.gethostbyname(hostname) #host take the value of own IP address
port = 65432
ThreadCount = 0

local_ip = socket.gethostbyname(hostname)
print(local_ip) #show server's IP address

try:
	ServerSideSocket.bind((host, port))
except socket.error as e:
	print(str(e))
print('Socket is listening..')

ServerSideSocket.listen(5)
temp_list = []


always=open("web.html","r")
alwayscontent=always.readlines()
always.close()
renew=open("renew.html","w")

for x in alwayscontent:
	renew.write(x) #copy web.html into renew.html
  
renew.close()


def multi_threaded_client(connection):
	connection.send(str.encode('Server is working:'))
	while True:
		data = connection.recv(1024) #receive message from client
		if not data:
			break
		l=data.decode()
		renew=open("renew.html","a")
		renew.write(l) #write the message(table) from client and put in renew.html
		renew.close()
	connection.close()

	
while True:
	Client, address = ServerSideSocket.accept()
	print('Connected to: ' + address[0] + ':' + str(address[1]))
	start_new_thread(multi_threaded_client, (Client, ))
	ThreadCount += 1
	print('Thread Number: ' + str(ThreadCount))
	
	
ServerSideSocket.close()
