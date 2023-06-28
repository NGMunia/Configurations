
import csv
from netmiko import ConnectHandler
from Device_list import access, core_sw



#Documenting Access_switches' interfaces and switchport access status:
with open('C:\\Users\\Munia-virtual\\Desktop\\Scripts\\Configurations\\Small Campus\\Docs.csv','w') as f:
    write_data = csv.writer(f)
    write_data.writerow(['hostname','interface','switchport'])
    
    for switches in access:
        net_connect=ConnectHandler(**switches)
        net_connect.enable()
        
        hostname = net_connect.send_command("show run | include hostname")
        write_data.writerow([hostname])

        for i in range(0,4):
            interface  = net_connect.send_command("show run | include interface Ethernet0/"+str(i))
            switchport = net_connect.send_command("show run interface ethernet0/"+str(i)+" | include switchport access")
            write_data.writerow(['',interface,switchport])


#Documenting Core SW:
with open('C:\\Users\\Munia-virtual\\Desktop\\Scripts\\Configurations\\Small Campus\\Core_sw.csv','w') as f:
    net_connect=ConnectHandler(**core_sw)
    net_connect.enable()

    write_data=csv.writer(f)
    write_data.writerow(['hostname','interface','switchport status','Address'])
    hostname = net_connect.send_command("show run | include hostname")
    write_data.writerow([hostname])

    for v in range (10,50,10):
        interface  = net_connect.send_command("show run | include Vlan"+str(v))
        ip_addr    = net_connect.send_command("show run int Vlan"+str(v)+" | include ip address")
        write_data.writerow(['',interface,'',ip_addr])
    
    for i in range (0,4):
        trunk_intf = net_connect.send_command("show run | include interface Ethernet0/"+str(i))
        port_status= net_connect.send_command("sh running-config interface e0/"+str(i)+" | include switchport mode")
        write_data.writerow(['',trunk_intf,port_status,''])









