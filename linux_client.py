import socket
import os
import re
import shutil
import psutil


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname) #ip address


file=open('/proc/cpuinfo',"r")
content=file.readlines()
cpu=content[4] 
cpu_regex=re.findall(":([^\]]+)CPU", cpu) #CPU name
speed_regex=re.findall("\@([^\]]+)GHz", cpu) #CPU speed
file.close()


total, used, free = shutil.disk_usage("/")
total=(total // (2**30)) #total RAM
used=(used // (2**30))
free=(free // (2**30)) #free RAM


temp = os.popen('sensors')
temp_output = temp.readlines()
temp_regex=re.findall("\+([^\]]+)", temp_output[16]) #CPU temperature


load = os.popen('uptime')
load_output = load.read()
load_regex=re.findall("load average: 0\,([0-9][0-9])", load_output) #CPU load


hdd_info = os.popen('df -h')
hdd_output = hdd_info.readlines()
hdd_regex=(hdd_output[7]).split()
HD_regex=re.findall("([0-9]*)G", hdd_regex[2]) #total Hard Disk
HD_free_regex=re.findall("([0-9]*)G", hdd_regex[3]) #free Hard Disk


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
   
#res = ClientMultiSocket.recv(1024)
while True:
   
    ClientMultiSocket.send(message.encode()) #send message(HTML table)
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()
