from netmiko import ConnectHandler
from rich import print as rprint
from Device_list import R1, R2, R3, R4, R5



#Configuring R4 router:
#    - LISP xTR
#    - MGRE tunnel (spoke)
#    - cryptography

rprint("======CONFIGURING R4 SPOKE ROUTER======\n")
net_connect=ConnectHandler(**R4)
net_connect.enable()
lisp=   [
            "router lisp",
            "ipv4 itr",
            "ipv4 etr",
            "ipv4 etr map-server 1.1.1.1 key cisco123",
            "ipv4 itr map-resolver 1.1.1.1",
            "database-mapping 192.168.10.0/24 172.31.1.10 priority 50 weight 50" ]
crypto= [
            "crypto isakmp policy 100",
            "hash sha",
            "authentication pre-share",
            "group 14",
            "lifetime 7200",
            "encryption aes",
            "crypto isakmp key abc123 address 0.0.0.0",
            "crypto ipsec transform-set crypt_ts esp-sha-hmac esp-aes 192",
            "mode transport",
            "crypto ipsec profile crypt_profile",
            "set transform-set crypt_ts" ] 
rprint(net_connect.send_config_set(lisp)+"\n")
rprint(net_connect.send_config_set(crypto))
net_connect.save_config()
net_connect.disconnect()



#Configuring R5 router:
#    - LISP xTR
#    - MGRE tunnel (spoke)
#    - cryptography

rprint("======CONFIGURING R5 SPOKE ROUTER======\n")
net_connect=ConnectHandler(**R5)
net_connect.enable()
lisp=   [
            "router lisp",
            "ipv4 itr",
            "ipv4 etr",
            "ipv4 etr map-server 1.1.1.1 key cisco123",
            "ipv4 itr map-resolver 1.1.1.1",
            "database-mapping 192.168.30.0/24 172.31.1.20 priority 50 weight 50" ]
crypto= [
            "crypto isakmp policy 100",
            "hash sha",
            "authentication pre-share",
            "group 14",
            "lifetime 7200",
            "encryption aes",
            "crypto isakmp key abc123 address 0.0.0.0",
            "crypto ipsec transform-set crypt_ts esp-sha-hmac esp-aes 192",
            "mode transport",
            "crypto ipsec profile crypt_profile",
            "set transform-set crypt_ts" ] 
rprint(net_connect.send_config_set(lisp)+"\n")
rprint(net_connect.send_config_set(crypto))
net_connect.save_config()
net_connect.disconnect()



#Configuring R2 router:
#    - MGRE tunnel (hub)
#    - cryptography

rprint("======CONFIGURING R4 HUB ROUTER======\n")
net_connect=ConnectHandler(**R2)
net_connect.enable()
tunnel= [
            "int tunnel 0",
            "tunnel source e1/0",
            "tunnel mode gre multipoint",
            "ip mtu 1400",
            "ip nhrp map multicast dynamic",
            "ip nhrp network-id 10",
            "ip nhrp authentication abc123",
            "ip address 172.31.1.1 255.255.255.0"  ]
crypto= [
            "crypto isakmp policy 100",
            "hash sha",
            "authentication pre-share",
            "group 14",
            "lifetime 7200",
            "encryption aes",
            "crypto isakmp key abc123 address 0.0.0.0",
            "crypto ipsec transform-set crypt_ts esp-sha-hmac esp-aes 192",
            "mode transport",
            "crypto ipsec profile crypt_profile",
            "set transform-set crypt_ts", ] 
rprint(net_connect.send_config_set(tunnel)+"\n")
rprint(net_connect.send_config_set(crypto)+"\n")
net_connect.save_config()
net_connect.disconnect()



#Configuring R1 router:
#    - LISP MS/MR

rprint("======CONFIGURING R4 MAP SERVER/RESOLVER======\n")
net_connect=ConnectHandler(**R1)
net_connect.enable()
lisp= [
        "router lisp",
        "ipv4 map-server",
        "ipv4 map-resolver",
        "site LISP_SITE_A",
        "authentication-key cisco123",
        "eid-prefix 192.168.10.0/24",
        "site LISP_SITE_B",
        "authentication-key cisco123",
        "eid-prefix 192.168.20.0/24",
        "site LISP_SITE_C",
        "authentication-key cisco123",
        "eid-prefix 192.168.30.0/24" ]
rprint(net_connect.send_config_set(lisp)+"\n")
net_connect.save_config()
net_connect.disconnect()




#Configuring R3 router:
#    - LISP xTR

rprint("======CONFIGURING R3 ROUTER======\n")
net_connect=ConnectHandler(**R3)
net_connect.enable()
lisp=   [
            "router lisp",
            "ipv4 itr",
            "ipv4 etr",
            "ipv4 etr map-server 1.1.1.1 key cisco123",
            "ipv4 itr map-resolver 1.1.1.1",
            "database-mapping 192.168.20.0/24 3.3.3.3 priority 50 weight 50" ]
rprint(net_connect.send_config_set(lisp)+"\n")
net_connect.save_config()
net_connect.disconnect()



