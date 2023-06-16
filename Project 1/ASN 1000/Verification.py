
from netmiko import ConnectHandler
from Device_list import A1000

net_connect=ConnectHandler(**A1000)
net_connect.enable()
command=input("Input show command: ")
print(net_connect._send_command_str(command))
