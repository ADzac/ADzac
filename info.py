import socket
import os
import re

from subprocess import check_output

#newfile = open('info.txt', "w")

#newfile.write(check_output("wmic diskdrive get size").decode())
#newfile.write(check_output("wmic logicaldisk get freespace").decode())
#newfile.write(str(check_output("systeminfo").decode()))
#newfile.write(str(check_output("wmic cpu get name").decode()))
#newfile.write(str(check_output("wmic cpu get maxclockspeed").decode()))
#newfile.write(str(check_output("wmic cpu get loadpercentage").decode()))

#newfile.close()


#def read_lines(_file):
#    grand_liste = []
#    for line in open_file(_file):
#        grand_liste.append(line)
#    return grand_liste


with open('info.txt', 'r') as f:
    l = f.readlines()
    
    cpu = (l[172])
    cpu_regex=re.findall("([^\]]+)CPU", cpu)
    
    cpu_speed = (l[181])
    cpu_speed = "{:.2f}".format(int(cpu_speed)/1000) 
    
    cpu_load = (l[190])
    
    ram_size = (l[75])
    ramsize_regex=re.findall("\:([^\]]+)MB", ram_size)
    free_ram = (l[77])
    freeram_regex=re.findall("\:([^\]]+)MB", free_ram)
    
    hd_size = (l[3])
    hd_size = "{:.0f}".format(int(hd_size)/1000000) 
    hd_free = (l[15])
    hd_free = "{:.0f}".format(int(hd_free)/1000000) 

# --------------------------------------------------------

message = """<!DOCTYPE html>
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
<td>Windows</td>
<td>""" + str(hd_size) + """</td>
<td>""" +str(hd_free)+"""</td>
<td>""" + str(ramsize_regex[0]) + """</td>
<td>""" + str(freeram_regex[0]) + """</td>
<td>""" + str(cpu_regex[0]) + """</td>
<td>""" + str(cpu_speed) + """</td>
<td>""" + str(cpu_load) + """</td>
<td>62</td>
<td><button class="button off">Off</button></td>
<td><button class="button restart">Restart</button></td>
</tr>



</table>

</body>
</html>
"""
# --------------------------------------------------------
webfile = open('web.html', "w")

webfile.write(message)

webfile.close()
