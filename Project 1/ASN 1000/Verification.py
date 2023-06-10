
from netmiko import ConnectHandler

from Device_list import A1000
net_connect=ConnectHandler(**A1000)
net_connect.enable()
ospf=net_connect.send_command("show ip ospf neighbor")
print(ospf)
print("\n")
bgp=net_connect.send_command("show ip bgp summary")
print(bgp)
