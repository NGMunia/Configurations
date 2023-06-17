
from netmiko import ConnectHandler
from rich import print as rprint
from Device_list import R3

#Verifying LISP

net_connect=ConnectHandler(**R3)
net_connect.enable()
commands=["ping 192.168.10.1 source 192.168.20.1","ping 192.168.30.1 source 192.168.20.1"]
for command in commands:
    rprint(net_connect.send_command(command)+"\n")

    

