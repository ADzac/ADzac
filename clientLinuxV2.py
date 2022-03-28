import socket
import os
import re
import shutil
import psutil
import tkinter
#importing the datetime module
from datetime import datetime
#using the now function to get the date and time value
date_time =datetime.now()
#using strftime() to get the current time value
current_time = date_time.strftime("%H:%M:%S")
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname) #ip address


file=open('/proc/cpuinfo',"r")
content=file.readlines()
cpu=content[4] 
cpu_regex=re.findall(":([^\]]+)CPU", cpu) #CPU name
speed_regex=re.findall("\@([^\]]+)GHz", cpu) #CPU speed
file.close()


total, used, free = shutil.disk_usage("/")
total=(total // (2**20)) #total RAM
used=(used // (2**20))
free=(free // (2**20)) #free RAM


temp = os.popen('sensors')
temp_output = temp.readlines()
temp_regex=re.findall("\+([^\]]+)", temp_output[15]) #CPU temperature


hello="hello"

load = os.popen('uptime')
load_output = load.read()
load_regex=re.findall("load average: 0\,([0-9][0-9])", load_output) #CPU load


hdd_info = os.popen('df -h')
hdd_output = hdd_info.readlines()
hdd_regex=(hdd_output[7]).split()
HD_regex=re.findall("([0-9]*)M", hdd_regex[2]) #total Hard Disk
HD_free_regex=re.findall("([0-9]*)M", hdd_regex[3]) #free Hard Disk

    
message="""
<tr>
<td>"""+current_time+"""</td>
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
<td><form onsubmit="Shutdown()">
    <input value="Shutdown" type="submit" />
  </form>
</td>
<td><form onsubmit="Restart()">
    <input value="Restart" type="submit" />
  </form>
</td>
  <script>
    function Shutdown() {
        alert(`Shutting Down`);
    }
    function Restart() {
        alert(`Restart`);
    }
  </script>
</td>
</tr>
"""



ClientMultiSocket = socket.socket()

host = input("Server's IP Address: ")  # The server's hostname or IP address
port = 65432  # The port used by the server


print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
ClientMultiSocket.send(message.encode()) #send message(HTML table)
#res = ClientMultiSocket.recv(1024)
while True:
    #ClientMultiSocket.send(message.encode()) #send message(HTML table)
	res = ClientMultiSocket.recv(2048)
	if res.decode() == "shutdown":
		os.system("/sbin/shutdown +1")
		print("Shutting Down")
	if res.decode() == "restart":
		os.system("/sbin/shutdown -r +1")
		print("Restarting")
	print(res.decode('utf-8'))
#ClientMultiSocket.close()
