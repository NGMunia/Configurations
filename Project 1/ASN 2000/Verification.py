from netmiko import ConnectHandler
from Device_list import C2000

net_connect=ConnectHandler(**C2000)
net_connect.enable()
command=input("Input show command: ")
print(net_connect._send_command_str(command))
