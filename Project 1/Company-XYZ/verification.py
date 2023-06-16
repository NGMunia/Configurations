
from netmiko import ConnectHandler
from Device_list import R1_Edge, firewall, R1_HUB, R1_LAN


print("=====verifying Edge router=====\n")
net_connect=ConnectHandler(**R1_Edge)
commands=["show ntp status", "show ip ospf neighbor", "show ip nat translations"]
for command in commands:
    print(net_connect.send_command(command)+"\n")
    

print("=====Verifying Firewall Router=====\n")
net_connect=ConnectHandler(**firewall)
net_connect.enable()
commands=["show policy-map type inspect zone-pair","show ip access-lists"]
for commands in commands:
    print(net_connect.send_command(commands))