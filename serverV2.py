from multiprocessing import connection
import socket
import os
from _thread import *
import tkinter

ServerSideSocket = socket.socket()
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 65432
ThreadCount = 0

print(host)

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
    print('Socket is listening..')

ServerSideSocket.listen(2)
temp_list = []

always=open("web.html","r")
alwayscontent=always.readlines()
always.close()
renew=open("renew.html","w")

for x in alwayscontent:
    renew.write(x)
renew.close()

def window():
    gui = tkinter.Tk()
    gui.geometry("300x300")
    btnRes = tkinter.Button(gui, text="Shutdown", command=lambda: restart(1))
    btnShut = tkinter.Button(gui, text="Restart", command=lambda: restart(2))
    btnRes.pack()
    btnShut.pack()
    gui.mainloop()
    #gui.update()

def restart(args):
    if args == 1:
        command = 'shutdown'
        Client.send(command.encode())
    if args == 2 :
        command = 'restart'
        Client.send(command.encode())
    else:
        exit()

def multi_threaded_client(connection):
    connection.send(('Server is working!!').encode())
    while True:
        data = connection.recv(2048)
        l=data.decode()
        #renew=open("web.html","a")
        f = open('renew.html','a')
        f.write(l)
        f.close()
        #renew.write(l)
        #renew.close()
        if not data:
            break
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    #while connected == True:
    window()
ServerSideSocket.close()
