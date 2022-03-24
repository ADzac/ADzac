import socket
import os
import re

from subprocess import check_output

newfile = open('info.txt', "w")

newfile.write(check_output("wmic diskdrive get size").decode())
newfile.write(check_output("wmic logicaldisk get freespace").decode())
#newfile.write(str(check_output("systeminfo").decode()))
newfile.write(str(check_output("wmic cpu get name").decode()))
newfile.write(str(check_output("wmic cpu get maxclockspeed").decode()))
newfile.write(str(check_output("wmic cpu get loadpercentage").decode()))

newfile.close()


#def read_lines(_file):
#    grand_liste = []
#    for line in open_file(_file):
#        grand_liste.append(line)
#    return grand_liste


with open('info.txt', 'r') as f:
    l = f.readlines()
    
    cpu = (l[33])
    cpu_regex=re.findall("([^\]]+)CPU", cpu)
    
    cpu_speed = (l[42])
    cpu_speed = "{:.2f}".format(int(cpu_speed)/1000) 
    
    cpu_load = (l[51])
    
    ram_size = (l[18])
    ramsize_regex=re.findall("\:([^\]]+)MB", ram_size)
    free_ram = (l[21])
    freeram_regex=re.findall("\:([^\]]+)MB", free_ram)
    
    hd_size = (l[3])
    hd_size = "{:.0f}".format(int(hd_size)/1000000) 
    hd_free = (l[12])
    hd_free = "{:.0f}".format(int(hd_free)/1000000)




#--------------------------------------------------------

message="""

<td>""" + str(hd_size) + """</td>
<td>""" +str(hd_free)+"""</td>
<td>""" + str(ramsize_regex) + """</td>
<td>""" + str(freeram_regex) + """</td>
<td>""" + str(cpu_regex[0]) + """</td>
<td>""" + str(cpu_speed) + """</td>
<td>""" + str(cpu_load) + """</td>
"""
#--------------------------------------------------------


ClientMultiSocket = socket.socket()


host = input("Server's IP Address: ")  # The server's hostname or IP address
port = 65432  # The port used by the server


print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
   
res = ClientMultiSocket.recv(1024)
while True:
   
    ClientMultiSocket.send(message.encode())
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()
