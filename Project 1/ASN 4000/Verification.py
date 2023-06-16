
from netmiko import ConnectHandler
from Device_list import B4000

net_connect=ConnectHandler(**B4000)
net_connect.enable()
command=input("Input show command: ")
print(net_connect._send_command_str(command))
