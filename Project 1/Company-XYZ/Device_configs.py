
from netmiko import ConnectHandler
from Device_list import R1_Edge, firewall, R1_HUB, R1_LAN


#Common configuration for all routers:
#    - SNMP configuration
#    - Control-plane policing
#    - Syslog
print("======Common configuration for all routers=====")
for devices in R1_Edge,R1_HUB,R1_LAN,firewall:
    net_connect=ConnectHandler(**devices)
    net_connect.enable()
    print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SNMP.txt")+"\n")
    print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\CoPP.txt")+"\n")
    print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SYSLOG.txt")+"\n")
   
    

#Common NTP configuration for HQ routers:
#    - R1_LAN, R2_Edge, Firewall, R1_HUB
print("======Configuring NTP on HQ routers=====")
for devices in firewall, R1_HUB, R1_LAN:
    net_connect=ConnectHandler(**devices)
    net_connect.enable()
    ntp_commands=["ntp server 10.1.1.10",
              "ntp update-calendar",
              "clock timezone GMT +3",
              "service timestamps log datetime localtime year",
              "service timestamps debug datetime year"]
    print(net_connect.send_config_set(ntp_commands)+"\n")



#Configuring Edge router:
#    - NAT/PAT
#    - NTP (server IP: 160.119.216.197)
print("======configuring Edge router=====")
net_connect=ConnectHandler(**R1_Edge)
net_connect.enable()
nat_conf=["ip access-list standard nat_acl",
          "permit 192.168.99.0 0.0.0.255",
          "int e0/0",
          "ip nat inside",
          "int e0/1",
          "ip nat outside",
          "ip nat inside source list nat_acl interface e0/1 overload"]
ntp_comm=["ip domain lookup",
          "ip name-server 8.8.8.8",
          "ntp server ke.pool.ntp.org",
          "ntp update-calendar",
          "clock timezone GMT +3",
          "service timestamps log datetime localtime year",
          "service timestamps debug datetime year"]
print(net_connect.send_config_set(ntp_comm)+"\n")
print(net_connect.send_config_set(nat_conf)+"\n")



#Configuring LAN Router
#    - QoS
#    - NetFlow
#    - DHCP
print("======Configuring LAN router=====")
net_connect=ConnectHandler(**R1_LAN)
net_connect.enable()
print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\QoS.txt")+"\n")
netflow_udp_port=input("netflow UDP port: ")
netflow=["ip flow-export version 9",
         "ip flow-export destination 192.168.255.254 "+netflow_udp_port,
         "ip flow-top-talkers",
         "top 10",
         "sort-by bytes",
         "int e0/1",
         "ip flow ingress",
         "ip flow egress",
         "service-policy output Internet_policy",
         "int e0/0",
         "ip helper-address 192.168.255.254"]
print(net_connect.send_config_set(netflow)+"\n")



#Configuring HUB router:
#    - Cryptography
#    - MGRE tunnel
print("======Configuring HUB router=====")
net_connect=ConnectHandler(**R1_HUB)
net_connect.enable()
print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\ISAKMP.txt")+"\n")
tunnel=["int tunnel 0",
        "bandwidth 1000",
        "ip address 172.31.1.1 255.255.255.0",
        "ip mtu 1400",
        "ip nhrp authentication xyzdmvpn",
        "ip nhrp map multicast dynamic",
        "ip nhrp network-id 10",
        "tunnel source Ethernet0/1",
        "tunnel mode gre multipoint",
        "ip ospf network broadcast",
        "ip ospf 1 area 0",
        "tunnel protection ipsec profile crypt_profile"]
print(net_connect.send_config_set(tunnel)+"\n")



#Configuring Firewalls:
#    - Zone based firewall
print("======Configuring Firewall router=====")
net_connect=ConnectHandler(**firewall)
net_connect.enable()
print(net_connect.send_config_from_file("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\ZBF.txt"))

net_connect.save_config()
net_connect.disconnect()