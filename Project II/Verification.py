
from netmiko import ConnectHandler
from rich import print as rprint
from Device_List import SW, R1, R2

for devices in R1,R2,SW:
    net_connect=ConnectHandler(**devices)
    net_connect.enable()
    command=input('\n'f'host {devices.get("host")}: input show command: ')
    rprint(net_connect._send_command_str(command)+'\n')
    