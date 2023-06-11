from netmiko import ConnectHandler

from Device_list import B4000
net_connect=ConnectHandler(**B4000)
net_connect.enable()
commands=["show ip bgp","show ip bgp summary"]
for i in commands:
    output=net_connect.send_command(i)
    print("\n")
    print(output)