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


#CoPP