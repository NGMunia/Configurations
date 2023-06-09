
#Configuring Firewalls (common configs):

from Devices import firewalls
from netmiko import ConnectHandler
for devices in firewalls:
    net_connect=ConnectHandler(**devices)
    net_connect.enable()
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\snmp.txt","r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\IPsla-echo.txt","r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Zone-based-firewall.txt" ,"r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\CoPP.txt","r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    nat_commands=["int e0/1","ip nat outside","int e0/0.255","ip nat inside","exit","ip access-list standard nat_acl","permit 10.1.20.0 0.0.0.255",
                  "permit 10.1.30.0 0.0.0.255","permit host 10.1.10.254","exit","ip nat inside source list nat_acl interface e0/1 overload","exit"]
    output=net_connect.send_config_set(nat_commands)    
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\NTP.txt" ,"r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    output=net_connect.save_config()
    


#Configuring LAN_routers:

from Devices import R1_LAN
for device in R1_LAN:
    net_connect=ConnectHandler(**device)
    net_connect.enable()
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\CoPP.txt","r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\snmp.txt","r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\QoS.txt","r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
    with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\NetFlow.txt","r") as f:
        read_data=f.readlines()
        output=net_connect.send_config_set(read_data)
        commands=["interface e0/2.255","service-policy output Internet_policy","ip flow ingress","ip flow egress"]
        output=net_connect.send_config_set(commands)
    ntp=["ntp server 10.1.255.254","ntp update-calendar","clock timezone GMT +3","service timestamps log datetime localtime year",
         "service timestamps debug datetime localtime year"]
    output=net_connect.send_config_set(ntp)
    output=net_connect.save_config()



#Configuring HSRP on Firewall routers:
#Firewall_1
firewall_1={'device_type':'cisco_ios',
            'host': '10.1.255.2',
            'username': 'Automation', 
            'secret': 'cisco123',
            'password':'cisco123'}
net_connect=ConnectHandler(**firewall_1)
net_connect.enable()
command=["track 1 ip sla 1","delay up 5 down 5","int e0/0.255","standby 1 version 2","standby 1 ip 10.1.255.254","standby 1 preempt",
        "standby 1 priority 110", "standby 1 track 1 decrement 30","standby 1 authentication key-string cisco123","exit"]
output=net_connect.send_config_set(command)
output=net_connect.send_command("show standby brief")


#Firewall_2
firewall_2={'device_type':'cisco_ios',
            'hostname':"10.1.255.3",
            'username': 'Automation', 
            'secret': 'cisco123',
            'password':'cisco123'}
net_connect=ConnectHandler(**firewall_2)
net_connect.enable()
command=["int e0/0.255","standby 1 version 2","standby 1 ip 10.1.255.254","standby 1 preempt",
         "standby 1 priority 90","standby 1 authentication key-string cisco123","exit"]
output=net_connect.send_config_set(command)
output=net_connect.send_command("show standby brief")
print(output)



#Configuring IPsec Tunneling:
#R1_VPN router
R1_VPN={'device_type': 'cisco_ios',
        'host': '10.1.1.2',
        'username': 'Automation', 
        'secret': 'cisco123',
        'password':'cisco123'}
net_connect=ConnectHandler(**R1_VPN)
net_connect.enable()
ipsec=["crypto isakmp policy 100",
       "hash sha",
       "group 14",
       "authentication pre-share",
       "lifetime 7200",
       "encryption aes",
       "crypto isakmp key cisco123 address 32.19.86.2",
       "crypto ipsec transform-set crypt_ts esp-sha-hmac esp-aes",
       "mode transport",
       "crypto ipsec profile crypt_profile",
       "set transform-set crypt_ts",
       "ip route 32.19.86.2 255.255.255.255 44.67.28.1"]
tunnel=["int e0/1",
        "ip address 44.67.28.2 255.255.255.252",
        "no shut",
        "int tunnel 0",
        "tunnel source e0/1",
        "tunnel-destination 32.19.86.2",
        "bandwidth 10000",
        "ip mtu 1400",
        "ip address 172.31.1.1 255.255.255.252",
        "ip ospf 1 area 0",
        "tunnel mode ipsec ipv4",
        "tunnel protection ipsec profile crypt_profile"]
output=net_connect.send_config_set(ipsec)
output=net_connect.send_config_set(tunnel)
ntp=["ntp server 10.1.255.254","ntp update-calendar","clock timezone GMT +3","service timestamps log datetime localtime year",
     "service timestamps debug datetime localtime year"]
output=net_connect.send_config_set(ntp)
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\CoPP.txt","r") as f:
    read_data=f.readlines()
    output=net_connect.send_config_set(read_data)
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\snmp.txt","r") as f:
    read_data=f.readlines()
    output=net_connect.send_config_set(read_data)
net_connect.save_config()
net_connect.disconnect()



#R2_VPN
R2_VPN={'device_type': 'cisco_ios',
        'host': '172.31.1.2',
        'username': 'Automation', 
        'secret': 'cisco123',
        'password':'cisco123'}
net_connect=ConnectHandler(**R2_VPN)
net_connect.enable()
LAN=["interface e0/0",
     "ip address 10.1.30.1 255.255.255.0",
     "ip ospf 1 area 30",
     "no shut"]
dhcp=["ip dhcp excluded-address 10.1.30.1 10.1.30.10",
      "ip dhcp pool Area 30",
      "network 10.1.30.0 255.255.255.0",
      "default-router 10.1.30.1",
      "dns-server 8.8.8.8",
      "lease 0 2"]
ntp=["ntp server 10.1.255.254","ntp update-calendar","clock timezone GMT +3","service timestamps log datetime localtime year",
     "service timestamps debug datetime localtime year"]
output=net_connect.send_config_set(ntp)
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\CoPP.txt","r") as f:
    read_data=f.readlines()
    output=net_connect.send_config_set(read_data)
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\snmp.txt","r") as f:
    read_data=f.readlines()
    output=net_connect.send_config_set(read_data)
output=net_connect.send_config_set(LAN)
output=net_connect.send_config_set(dhcp)
net_connect.save_config()
