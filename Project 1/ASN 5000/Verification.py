
from netmiko import ConnectHandler
from Device_list import A5000

net_connect=ConnectHandler(**A5000)
show_commands=["show ip bgp", "show ip bgp summary"]
for i in show_commands:
    output=net_connect.send_command(i)
    print(output)
    print("\n")
    