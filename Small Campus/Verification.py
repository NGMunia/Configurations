
from netmiko import ConnectHandler
from Device_list import core_sw, R1_Edge, FW_1
from rich import print as rprint


for devices in core_sw, R1_Edge, FW_1:
    connect = ConnectHandler(**devices)
    connect.enable()
    commands = input(f'Host: {devices.get("ip")} input command: ')
    rprint(connect._send_command_str(commands)+'\n')




