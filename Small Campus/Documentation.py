
from netmiko import ConnectHandler
from Device_list import core_sw, SW1,SW2,SW3,SW4,R1_Edge,FW_1
from rich import print as rprint
import csv

#Documenting Serial numbers, Image, and Version

with open('C:\\Users\\Munia-virtual\\Desktop\\Scripts\\Configurations\\Small Campus\\Devices_doc.csv','w',newline='') as f:
        write_data = csv.writer(f)
        write_data.writerow(['Hostname','Version','Image','Serial-No','Uptime'])
        
        for devices in core_sw,SW1,SW2,SW3,SW4,FW_1,R1_Edge: 
            net_connect=ConnectHandler(**devices)
            net_connect.enable()

            output  = net_connect.send_command("show version",use_textfsm=True)[0]

            hostname = output.get("hostname")
            version = output.get("version")
            image = output.get("running_image")
            serial = output.get("serial")
            uptime = output.get("uptime")

            write_data.writerow([hostname,version,image,serial,uptime])
           

            

            