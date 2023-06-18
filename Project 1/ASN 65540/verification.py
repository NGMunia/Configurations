
from netmiko import ConnectHandler
from rich import print as rprint
from Device_list import R_1

net_connect=ConnectHandler(**R_1)
net_connect.enable()
commands=input("Input show command: ")
print(net_connect._send_command_str(commands))