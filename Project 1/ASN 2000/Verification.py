from netmiko import ConnectHandler
from Device_list import C2000

net_connect=ConnectHandler(**C2000)
net_connect.enable()
show_commands=[ "show ip bgp "]
for i in show_commands:
    output=net_connect.send_command(i)
    print("\n")
    print(output)
   