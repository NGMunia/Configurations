
from netmiko import ConnectHandler
from Device_list import RTR1, RTR2

#Tunnel security parameters:
with open ("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Multicast over IPsec VTI\\Crypto.txt", "w") as c:
    c.write("crypto isakmp policy 10\n")
    c.write("hash sha\n")
    c.write("authentication pre-share\n")
    c.write("group 14\n")
    c.write("lifetime 7200\n")
    c.write("encryption aes\n")


net_connect=ConnectHandler(**RTR1)
net_connect.enable()
tunnel =   [
                "int tunnel 0",
                "ip mtu 1400",
                "tunnel source e0/1",
                "tunnel destination 17.17.17.2",
                "ip ad"
           ]













with open ("C:\\Users\\Munia-Virtual\\Desktop\\Scripts\\Configurations\\Project 1\\Multicast over IPsec VTI\\Crypto.txt", "r") as c:
    read_data=c.readlines()
    print(read_data)
