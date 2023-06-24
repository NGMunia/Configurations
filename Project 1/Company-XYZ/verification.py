
from netmiko import ConnectHandler
from Device_list import R1_Edge, firewall, R1_HUB, R1_LAN,spokes
from rich import print as rprint


net_connect=ConnectHandler(**R1_HUB)
net_connect.enable()
rprint(net_connect.send_command("ping 172.31.1.255 repeat 1")+"\n")


for devices in spokes:
    net_connect=ConnectHandler(**devices)
    net_connect.enable()
    rprint(net_connect.send_command("show ip route ospf")+"\n\n")