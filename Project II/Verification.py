
from netmiko import ConnectHandler
from rich import print as rprint
from Device_List import SW, R1, R2

for devices in SW, R1, R2:
    net_connect=ConnectHandler(**devices)
    net_connect.enable()
    commands=input(f'Host {devices.get("host")}: Input show command: ')
    rprint(net_connect._send_command_str(commands)+'\n')
    