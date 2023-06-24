
from netmiko import ConnectHandler
from Device_list import spokes

#Spoke/Branch routers configuration:
#    - SNMP 
#    - CoPP
#    - Syslog
#    - NetFlow
print("======Configuring Spoke routers======\n")
for routers in spokes:
    net_connect=ConnectHandler(**routers)
    net_connect.enable()
    
    print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SNMP.txt")+"\n")
    print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\CoPP.txt")+"\n")
    print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SYSLOG.txt")+"\n")

    ip=input(f'spoke {routers.get("host")} LAN ip address: ')
    ospf_area=input(f'spoke {routers.get("host")} ospf area: ')
    
    lan_conf=["int e0/0",
              "ip address "+ip,
              "ip ospf 1 area "+ospf_area,
              "no shut"]
    print(net_connect.send_config_set(lan_conf)+"\n")
    udp_port=int(input(f'{routers.get("host")} udp port: '))
    netflow=["ip flow-export version 9",
             "ip flow-export destination 192.168.255.254 "+str(udp_port),
             "ip flow-top-talkers",
             "top 5",
             "sort-by bytes",
             "ip flow-cache timeout active 1",
             "int e0/0",
             "ip nbar protocol-discovery",
             "ip flow ingress",
             "ip flow egress"]
    print(net_connect.send_config_set(netflow)+"\n")
    ntp_commands=["ntp server 172.31.1.1",
              "ntp update-calendar",
              "clock timezone GMT +3",
              "service timestamps log datetime localtime year",
              "service timestamps debug datetime localtime year"]
    print(net_connect.send_config_set(ntp_commands))
    net_connect.save_config()
    net_connect.disconnect()



#EEM applet:
for devices in spokes:
    net_connect=ConnectHandler(**devices)
    net_connect.enable()
    filename = input(f'Host {devices.get("host")} TFTP filename: ')
    EEM      = ["event manager environment tftpserver tftp://192.168.255.254/",
                "event manager environment filename "+filename,
                "event manager applet AUTOMATIC_BACKUP_CONFIG",
                "event timer cron cron-entry \"0 11 * * 1-6\"",
                "action 1.0 cli command \"enable\"",
                "action 1.1 cli command \"debug event manager action cli\"",
                "action 1.2 cli command \"conf t\"",
                "action 1.3 cli command \"file prompt quiet\"",
                "action 1.4 cli command \"do copy start $tftpserver$filename\"",
                "action 1.5 cli command \"no file prompt quiet\"",
                "action 1.6 syslog priority informational msg \"TFTP backup successful!!\""]
    print(net_connect.send_config_set(EEM)+"\n")
    net_connect.save_config()
    net_connect.disconnect()
