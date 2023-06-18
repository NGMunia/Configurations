
from netmiko import ConnectHandler
from Device_list import RTR1, RTR2
from rich import print as rprint



#Configuring RTR-1 router
net_connect=ConnectHandler(**RTR1)
net_connect.enable()
tunnel =   [
                "int tunnel 0",
                "ip mtu 1400",
                "tunnel source e0/1",
                "tunnel destination 17.17.17.2",
                "ip address 172.31.1.1 255.255.255.252",
                "ip ospf 1 area 0"    ]
multicast= [
                "ip multicast-routing",
                "int range e0/0, tunnel0",
                "ip pim sparse-mode",
                "ip pim rp-address 192.168.10.1" ]
lan_intf = [" int e0/0", "ip ospf 1 area 10","router ospf 1", "router-id 172.31.1.1"]
commands=[tunnel, multicast, lan_intf]
for commands in commands:
    rprint(net_connect.send_config_set(commands)+"\n")
    net_connect.save_config()



#Configuring RTR-2 router:
net_connect=ConnectHandler(**RTR2)
net_connect.enable()
tunnel =   [
                "int tunnel 0",
                "ip mtu 1400",
                "tunnel source e0/1",
                "tunnel destination 200.165.201.10",
                "ip address 172.31.1.2 255.255.255.252",
                "ip ospf 1 area 0"]
lan_intf = [" int e0/0", "ip ospf 1 area 99"]
multicast= [
                "ip multicast-routing",
                "int range e0/0, tunnel0",
                "ip pim sparse-mode",
                "int e0/0",
                "ip igmp join-group 239.1.10.100",
                "ip pim rp-address 192.168.10.1" ]
commands=[tunnel, multicast, lan_intf]
for commands in commands:
    rprint(net_connect.send_config_set(commands)+"\n")
    net_connect.save_config()



#Cryptography:
peer_address=input("Peer address: ")
crypto_commands=["crypto isakmp policy 10",
                 "hash sha",
                 "authentication pre-share",
                 "group 14",
                 "lifetime 7200",
                 "encryption aes",
                 "crypto isakmp key cisco123 address "+peer_address,
                 "crypto ipsec transform-set crypt_ts esp-sha-hmac esp-aes 192",
                 "mode transport",
                 "crypto ipsec profile crypt_profile",
                 "set transform-set crypt_ts"]
rprint(net_connect.send_config_set(crypto_commands))






