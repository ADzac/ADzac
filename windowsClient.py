import socket
import os
import re
import platform
from subprocess import check_output

newfile = open('info.txt', "w")

newfile.write(check_output("wmic diskdrive get size").decode())
newfile.write(check_output("wmic logicaldisk get freespace").decode())
newfile.write(str(check_output("systeminfo").decode('utf_8', 'ignore')))
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
    
    cpu = (l[136])
    cpu_regex=re.findall("([^\]]+)CPU", cpu)
    
    cpu_speed = (l[145])
    cpu_speed = "{:.2f}".format(int(cpu_speed)/1000) 
    
    cpu_load = (l[154])
    
    ram_size = (l[75])
    ramsize_regex=re.findall("\:([^\]]+)M", ram_size)
    free_ram = (l[77])
    freeram_regex=re.findall("\:([^\]]+)M", free_ram)
    
    hd_size = (l[3])
    hd_size = "{:.0f}".format(float(hd_size)/1000000) 
    hd_free = (l[12])
    hd_free = "{:.0f}".format(float(hd_free)/1000000)




#--------------------------------------------------------

message="""
<tr>
<td>""" + str(socket.gethostbyname(socket.gethostname())) + """</td>
<td>""" + str(platform.system()) + """</td>
<td>""" + str(hd_size) + """</td>
<td>""" +str(hd_free)+"""</td>
<td>""" + str(ramsize_regex[0]) + """</td>
<td>""" + str(freeram_regex[0]) + """</td>
<td>""" + str(cpu_regex[0]) + """</td>
<td>""" + str(cpu_speed) + """</td>
<td>""" + str(cpu_load) + """</td>
<td>""" + str(cpu_load) + """</td>
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
   
    res = ClientMultiSocket.recv(1024)
    while True:
        ClientMultiSocket.send(message.encode())
        res = ClientMultiSocket.recv(1024)
        print(res.decode('utf_8', 'ignore'))
except KeyboardInterrupt:
    ClientMultiSocket.close()
    print("Keyboard interrupt exception caught")
