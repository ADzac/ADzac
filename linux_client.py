import socket



import os
import re

import shutil
import psutil

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


file=open('/proc/cpuinfo',"r")


content=file.readlines()

cpu=content[4]
cpu_regex=re.findall(":([^\]]+)CPU", cpu)
speed_regex=re.findall("\@([^\]]+)GHz", cpu)
file.close()


total, used, free = shutil.disk_usage("/")


temp = os.popen('sensors')
temp_output = temp.readlines()
temp_regex=re.findall("\+([^\]]+)", temp_output[16])



load = os.popen('uptime')
load_output = load.read()
#load_regex=re.findall("load average: 0\,([^\]]+)\,", load_output)
load_regex=re.findall("load average: 0\,([0-9][0-9])", load_output)

total=(total // (2**30))
used=(used // (2**30))
free=(free // (2**30))
#hdd=str(psutil.virtual_memory().total /1000000)
#hdd_regex = "{:.2f}".format(float(hdd)) 

hdd_info = os.popen('df -h')
hdd_output = hdd_info.readlines()
hdd_regex=(hdd_output[7]).split()
HD_regex=re.findall("([0-9]*)G", hdd_regex[2])
HD_free_regex=re.findall("([0-9]*)G", hdd_regex[3])



#--------------------------------------------------------

message="""
<tr>
<td>"""+local_ip+"""</td>
<td>Linux</td>
<td>"""+HD_regex[0]+"""000</td>
<td>"""+HD_free_regex[0]+"""000</td>
<td>"""+str(total)+"""</td>
<td>"""+str(free)+"""</td>
<td>"""+str(cpu_regex[0])+"""</td>
<td>"""+str(speed_regex[0])+"""</td>
<td>"""+str(load_regex[0])+"""</td>
<td>"""+str(temp_regex[0])+"""</td>
<td>shutdown</td>
<td>Restart</td>
</tr>
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
