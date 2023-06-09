

from netmiko import ConnectHandler
from Devices import R1_LAN
from Devices import VPN_routers
from Devices import firewalls

#R1_LAN
for router in R1_LAN:
    net_connect=ConnectHandler(**router)
    net_connect.enable()
    response=net_connect.send_command("show startup-conf")
    print(response)
    print("\n")
#Firewalls
for firewall in firewalls:
    net_connect=ConnectHandler(**firewall)
    net_connect.enable()
    response=net_connect.send_command("show startup-conf")
    print(response)
    print("\n")
#VPN_routers
for vpn in VPN_routers:
    net_connect=ConnectHandler(**vpn)
    net_connect.enable()
    response=net_connect.send_command("show startup-conf")
    print(response)















