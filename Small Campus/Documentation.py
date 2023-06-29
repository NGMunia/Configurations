
from netmiko import ConnectHandler
from Device_list import R1_Edge,core_sw, FW_1
import csv

#Documenting Serial numbers, Image, and Version

with open('C:\\Users\\Munia-virtual\\Desktop\\Scripts\\Configurations\\Small Campus\\Routers.csv','w',newline='') as f:
        write_data = csv.writer(f)
        write_data.writerow(['Hostname','Version','Image','Serial'])
        
        for devices in R1_Edge,core_sw,FW_1: 
            net_connect=ConnectHandler(**devices)
            net_connect.enable()

            hostname = net_connect.send_command("show run | include hostname")
            output = net_connect.send_command("show version",use_textfsm=True)[0]
            version= output.get("version")
            image = output.get("running_image")
            serial = output.get("serial")
            
            write_data.writerow([hostname,version,image,serial])
