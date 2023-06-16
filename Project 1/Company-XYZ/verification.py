
from netmiko import ConnectHandler
from Device_list import R1_Edge, firewall, R1_HUB, R1_LAN
from rich import print as rprint


print("=====verifying Edge router=====\n")
net_connect=ConnectHandler(**R1_Edge)
net_connect.enable()
commands=input("Edge-Router\ninput show command: ")
rprint(net_connect._send_command_str(commands)+"\n")
    

print("=====Verifying HUB Router=====\n")
net_connect=ConnectHandler(**R1_HUB)
net_connect.enable()
commands=input("HUB-router\ninput show command: ")
rprint(net_connect._send_command_str(commands))