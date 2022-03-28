import socket
import os
import re
import platform
from subprocess import check_output
import time

newfile = open('info.txt', "w") #write all necessary stats in info.txt

newfile.write(check_output("wmic diskdrive get size").decode())
newfile.write(check_output("wmic logicaldisk get freespace").decode())
newfile.write(str(check_output("systeminfo").decode('utf_8', 'ignore')))
newfile.write(str(check_output("wmic cpu get name").decode()))
newfile.write(str(check_output("wmic cpu get maxclockspeed").decode()))
newfile.write(str(check_output("wmic cpu get loadpercentage").decode()))

newfile.close()


with open('info.txt', 'r') as f:
    l = f.readlines()
    
    cpu = (l[139])
    cpu_regex=re.findall("([^\]]+)CPU", cpu) #CPU name
    
    cpu_speed = (l[148])
    cpu_speed = "{:.2f}".format(int(cpu_speed)/1000) #CPU speed
    
    cpu_load = (l[157]) #CPU load
    
    ram_size = (l[78])
    ramsize_regex=re.findall("\:([^\]]+)M", ram_size) #total RAM
    free_ram = (l[80])
    freeram_regex=re.findall("\:([^\]]+)M", free_ram) #free RAM
    
    hd_size = (l[3])
    hd_size = "{:.0f}".format(float(hd_size)/1000000)  #total Hard Disk
    hd_free = (l[12])
    hd_free = "{:.0f}".format(float(hd_free)/1000000) #free Hard Disk

    
#--------------------------------------------------------

message="""
<tr><td>"""+time.strftime('%X')+"""</td>
<td>""" + str(socket.gethostbyname(socket.gethostname())) + """</td> 
<td>""" + str(platform.system()) + """</td>
<td>""" + str(hd_size) + """</td>
<td>""" +str(hd_free)+"""</td>
<td>""" + str(ramsize_regex[0]) + """</td>
<td>""" + str(freeram_regex[0]) + """</td>
<td>""" + str(cpu_regex[0]) + """</td>
<td>""" + str(cpu_speed) + """</td>
<td>""" + str(cpu_load) + """</td>
<td>30°C</td>
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
#--------------------------------------------------------


ClientMultiSocket = socket.socket()

try:
    host = input("Server's IP Address: ")  # The server's hostname or IP address
    port = 65432  # The port used by the server

    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    
    ClientMultiSocket.send(message.encode())
   
    
    while True:
        res = ClientMultiSocket.recv(2048)
        print(res.decode('utf_8', 'ignore'))
    
    
        if res.decode() == "shutdown" :
            os.system("shutdown /s /t 10")
            print("Shutting Down")
        if res.decode() == "restart" :
            os.system("shutdown /r /t 10")
            print("Restarting")
            
except KeyboardInterrupt or res.decode() == "shutdown" :
    ClientMultiSocket.close()
    print("Keyboard interrupt exception caught")
    
