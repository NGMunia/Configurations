
with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Zone-based-firewall.txt","x") as f:
    f.write("ip access-list extended zbf-acl\n")
    f.write("permit tcp any any eq 443\n")
    f.write("permit tcp any any eq 80\n")
    f.write("permit icmp any any echo-reply\n")
    f.write("permit udp any any\n")
    f.write("exit\n")

    f.write("class-map type inspect Inside_Outside_class\n")
    f.write("match access-group name zbf-acl\n")
    f.write("exit\n")
    f.write("policy-map type inspect Inside_Outside_Policy\n")
    f.write("class Inside_Outside_class\n")
    f.write("inspect\n")
    f.write("exit\n")

    f.write("zone-security Inside\n")
    f.write("sone-security Outside\n")
    f.write("interface e0/0.255\n")
    f.write("zone-member security Inside\n")
    f.write("interface e0/1\n")
    f.write("zone-member security Outside\n")

    f.write("zone-pair security Inside_Outside_Zone\n")
    f.write("service-policy type inspect Inside_Outside_Policy\n")
    f.write("end\n")
    f.write("write memory\n")

with open("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Zone-based-firewall.txt", "r") as f:
    read_data=f.read()
    print(read_data)
