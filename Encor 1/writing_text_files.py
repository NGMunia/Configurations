
#NetFlow configuration text
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\NetFlow.txt","w") as f:
    f.write("ip flow-export version 9\n")
    f.write("ip flow-export destination 10.1.10.254 9996\n")
    f.write("ip flow-top-talkers\n")
    f.write("top 5\n")
    f.write("sort-by bytes\n")
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\NetFlow.txt","r") as f:
    read_data=f.read()
    print(read_data)


#IPSLA configuration text
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\IPsla-echo.txt","r") as f:
    output=f.read()
    print(output)


#Zone-based firewall configuration text
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Zone-based-firewall.txt" ,"r") as f:
    output=f.read()
    print(output)


#NTP configuration text
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\NTP.txt" ,"w") as f:
    f.write("ip domain lookup\n")
    f.write("ip name-server 8.8.8.8\n")
    f.write("ip name-server 8.8.4.4\n")
    f.write("ntp server ke.pool.ntp.org\n")
    f.write("ntp update-calendar\n")
    f.write("clock timezone GMT +3\n")
    f.write("service timestamps log datetime localtime year\n")
    f.write("service timestamps debug datetime localtime year\n")
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\NTP.txt","r") as f:
    read_data=f.read()
    print(read_data)


#SNMP configuration text
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\snmp.txt","r") as f:
    output=f.read()
    print(output)


#CoPP configuration text:
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\CoPP.txt", "w") as f:
    f.write("ip access-list extended Copp_routing_acl\n")
    f.write("permit ospf any host 224.0.0.6\n")
    f.write("permit ospf any host 224.0.0.5\n")
    f.write("ip access-list extended Copp_icmp_acl\n")
    f.write("permit icmp any any\n")
    f.write("ip access-list extended Copp_management_acl\n")
    f.write("permit udp host 10.1.10.254 any eq 161\n")
    f.write("permit tcp any any eq 22\n")
    f.write("class-map match-any Copp_routing_class\n")
    f.write("match access-group name Copp_routing_acl\n")
    f.write("class-map match-any Copp_icmp_class\n")
    f.write("match access-group name Copp_icmp_acl\n")
    f.write("class-map match-any Copp_management_class\n")
    f.write("match access-group name Copp_management_acl\n")
    f.write("policy-map Copp_policy\n")
    f.write("class Copp_routing_class\n")
    f.write("police 64k conform-action transmit exceed-action transmit\n")
    f.write("class Copp_icmp_class\n")
    f.write("police 8k conform-action transmit exceed-action drop\n")
    f.write("class Copp_management_class\n")
    f.write("police 128k conform-action transmit exceed-action transmit\n")
    f.write("control-plane\n")
    f.write("service-policy input Copp_policy\n")
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\CoPP.txt","r") as f:
    read_data=f.read()
    print(read_data)


#QoS classification/Marking/policing:
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\QoS.txt","w") as f:
    f.write("class-map match-any Scavenger-class\n")
    f.write("match protocol netflix\n")
    f.write("match protocol bittorrent\n")
    f.write("class-map match-any social-media-class\n")
    f.write("match protocol facebook\n")
    f.write("match protocol twitter\n")
    f.write("match protocol instagram\n")
    f.write("class-map match-any mission-critical-class\n")
    f.write("match protocol dns\n")
    f.write("policy-map Internet_policy\n")
    f.write("class Scavenger-class\n")
    f.write("drop\n")
    f.write("class social-media-class\n")
    f.write("set dscp cs1\n")
    f.write("police 64k conform-action transmit exceed-action drop\n")  
    f.write("class mission-critical-class\n")
    f.write("set dscp af31\n")
    f.write("bandwidth percent 20\n") 
    f.write("class class-default\n")
    f.write("set dscp default\n")
    f.write("fair-queue\n") 
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\QoS.txt","r") as f:
    read_data=f.read()
    print(read_data)


#Zone based firewall
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Zone-based-firewall.txt","x") as f:
    f.write("ip access-list extended zbf-acl\n")
    f.write("permit tcp any any eq 443\n")
    f.write("permit tcp any any eq 80\n")
    f.write("permit icmp any any echo-reply\n")
    f.write("permit udp any any\n")

    f.write("class-map type inspect Inside_Outside_class\n")
    f.write("match access-group name zbf-acl\n")
    f.write("policy-map type inspect Inside_Outside_Policy\n")
    f.write("class Inside_Outside_class\n")
    f.write("inspect\n")

    f.write("zone-security Inside\n")
    f.write("zone-security Outside\n")
    f.write("interface e0/0.255\n")
    f.write("zone-member security Inside\n")
    f.write("interface e0/1\n")
    f.write("zone-member security Outside\n")

    f.write("zone-pair security Inside_Outside_Zone\n")
    f.write("service-policy type inspect Inside_Outside_Policy\n")


with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Zone-based-firewall.txt", "r") as f:
    read_data=f.read()
    print(read_data)











































































































