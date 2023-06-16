

#SPOKE/BRANCH ROUTERS CONFIGURATIONS:

from netmiko import ConnectHandler
from Device_list import spokes


for routers in spokes:
    net_connect=ConnectHandler(**routers)
    net_connect.enable()
    ike_phase_1=[
                   "crypto isakmp policy 100",
                   "hash sha",
                   "authentication pre-share",
                   "group 14",
                   "lifetime 7200",
                   "encryption aes",
                   "crypto isakmp key xyzdmvpn address 0.0.0.0 0.0.0.0"
                ]
    ike_phase_2=[
                   "crypto ipsec transform-set crypt_ts esp-sha-hmac esp-aes 192",
                   "mode transport",
                   "crypto ipsec profile crypt_profile",
                   "set transform-set crypt_ts"
                ]
    output=net_connect.send_config_set(ike_phase_1)
    print(output)
    print("\n")
    output=net_connect.send_config_set(ike_phase_2)
    print(output)
    print("\n")
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\configurations\\Project 1\\Company-XYZ\\NTP.txt","r") as f:    #NTP configuration (NTP server:HUB IP )
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
        print(output)
        print('\n')
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SNMP.txt","r") as f:   #SNMP configuration
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
        print(output)
        print('\n')
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\CoPP.txt","r") as f:   #CoPP configuration
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
        print(output)
        print('\n')
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SYSLOG.txt","r") as f: #Syslog configurarion
        read_data=f.read()
        output=net_connect.send_config_set(read_data)
        print(output)
       