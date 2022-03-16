import socket
import os


import shutil
import psutil

file=open('/proc/cpuinfo',"r")


content=file.readlines()

#newfile=open('info.txt',"w")
#newfile.write(content[4])
cpu=content[4]
file.close()


total, used, free = shutil.disk_usage("/")



#newfile.write("Total: %d GiB" % (total // (2**30)))
#newfile.write("Used: %d GiB" % (used // (2**30)))
#newfile.write("Free: %d GiB" % (free // (2**30)))
#newfile.write(str(psutil.virtual_memory().total /1000000000))

#newfile.close()
#total="Total: %d GiB" % (total // (2**30))
#used="Used: %d GiB" % (used // (2**30))
#free="Free: %d GiB" % (free // (2**30))

total=(total // (2**30))
used=(used // (2**30))
free=(free // (2**30))
hdd=str(psutil.virtual_memory().total /1000000000)







#--------------------------------------------------------

message="""<!DOCTYPE html>
<html lang="en" >
<head>
<meta charset="utf-8">
<!--<link rel="stylesheet" href="xxx.css">-->
<title>Monitoring Parc Machines</title>
                <link rel="icon" type="image/png" href="https://aws.wideinfo.org/upblog.com.au/wp-content/uploads/2022/03/04134822/whatisacomputer_desktop_computers.jpg">
<style>

table, th, td {
border: 1px solid white;
border-collapse: collapse;
}

th {
background-color: #1D70B9;
color: white;
}

tr:nth-child(even) {
background-color: #D6EEEE;
}

th, td {
text-align: center;
padding: 8px;
}
.button {
border: none;
color: white;
padding: 16px 32px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 16px;
margin: 4px 2px;
transition-duration: 0.4s;
cursor: pointer;
}

.restart {
background-color: white;
color: black;
border: 2px solid #008CBA;
}

.restart:hover {
background-color: #008CBA;
color: white;
}

.off{
background-color: white;
color: black;
border: 2px solid #EE2647;
}
.off:hover {
background-color: #EE2647;
color: white;
}

.on{
background-color: white;
color: black;
border: 2px solid #35EF1F;
}
.on:hover {
background-color: #35EF1F;
color: white;
}

</style>
</head>
<body>
<table style="width:100%">
<tr>
<th>Appareil</th>
<th>OS</th>
<th>HD size(Mo)</th>
<th>Free Space(Mo)</th>
<th>RAM size(Go)</th>
<th>Free memory(Go)</th>
<th>CPU</th>
<th>CPU speed(GHz)</th>
<th>CPU load(%)</th>
<th>CPU Temp.(°C)</th>
<th>ShutDown</th>
<th>Restart</th>
</tr>
<tr>
<td>PC-1</td>
<td>Linux</td>
<td>1000</td>
<td>"""+str(hdd)+"""</td>
<td>"""+str(total)+"""</td>
<td>"""+str(free)+"""</td>
<td>"""+str(cpu)+"""</td>
<td>2,7</td>
<td>20</td>
<td>62</td>
<td><button class="button off">Off</button></td>
<td><button class="button restart">Restart</button></td>
</tr>

 
 
</table>

</body>
</html>
"""
#--------------------------------------------------------

HOST = input("Server's IP Address: ")  # The server's hostname or IP address
PORT = 65432  # The port used by the server

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    #f = open("info.txt","r")
    #l = f.read()
    
    #s.send(l.encode())
    #s.send(cpu.encode())
    #s.send(total.encode())
    #s.send(free.encode())
    #s.send(hdd.encode())
    #s.send(used.encode())
    #f.close()
    s.send(message.encode())
