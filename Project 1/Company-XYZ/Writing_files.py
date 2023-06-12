#COMMON CONFIGS:

#SNMP configuration:
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SNMP.txt","w") as f:
    f.write("ip access-list standard snmp-acl\n")
    f.write("permit host 192.168.255.254\n")
    f.write("snmp-server system-shutdown\n")
    f.write("snmp-server community xyz_routers ro snmp-acl\n")
    f.write("snmp-server enable traps config\n")
    f.write("snmp-server host 192.168.255.254 traps version 2c xyz_routers\n")
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SNMP.txt","r") as f:
    read_data=f.read()
    print(read_data)


#Syslog
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SYSLOG.txt","w") as f:
    f.write("logging monitor informational\n")
    f.write("logging host 192.168.255.254\n")
    f.write("logging trap\n")
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\SYSLOG.txt","r") as f:
    read_data=f.read()
    print(read_data)


#Control-plane policing:
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\CoPP.txt","w") as f:
    f.write("ip access-list extended Copp_routing_acl\n")
    f.write("permit ospf any host 224.0.0.6\n")
    f.write("permit ospf any host 224.0.0.5\n")

    f.write("ip access-list extended Copp_icmp_acl\n")
    f.write("permit icmp any any\n")
    f.write("ip access-list extended Copp_management_acl\n")
    f.write("permit udp host 192.168.255.254 any eq 161\n")
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
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\CoPP.txt","r") as f:
    read_data=f.read()
    print(read_data)



#QoS:
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Company-XYZ\\QoS.txt","w") as f:
    f.write("ip access-list extended Server-access-acl\n")
    f.write("permit ip any host 192.168.255.254\n")
    f.write("class-map match-any Scavenger-class\n")
    f.write("match protocol netflix\n")
    f.write("match protocol bittorrent\n")

    f.write("class-map match-any social-media-class\n")
    f.write("match protocol facebook\n")
    f.write("match protocol twitter\n")
    f.write("match protocol instagram\n")
    f.write("class-map match-any mission-critical-class\n")
    f.write("match protocol dns\n")
    f.write("match access-group name Server-access-acl\n")

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

