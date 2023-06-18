
from netmiko import ConnectHandler
from rich import print as rprint
from Device_list import R_1, R_2, R_3



#Configuring BGP
#R_1 is the Route reflector.
net_connect=ConnectHandler(**R_1)
net_connect.enable()
bgp_comms = [
                "router bgp 65000",
                "neighbor 2.2.2.2 remote-as 65000",
                "neighbor 2.2.2.2 update-source lo0",
                "neighbor 2.2.2.2 route-reflector-client",
                "neighbor 3.3.3.3 remote-as 65000",
                "neighbor 3.3.3.3 update-source lo0",
                "neighbor 3.3.3.3 route-reflector-client" ]
rprint(net_connect.send_config_set(bgp_comms)+"\n")
net_connect.save_config()



#Configuring BGP on R_2:
net_connect=ConnectHandler(**R_2)
net_connect.enable()
bgp_comms = [
                "router bgp 65000",
                "neighbor 1.1.1.1 remote-as 65000",
                "neighbor 1.1.1.1 update-source lo0",
                "neighbor 1.1.1.1 next-hop-self",
                "neighbor 32.19.86.5 remote-as 3000",
                "network 17.17.17.0 mask 255.255.255.252",
                "aggregate-address 17.17.17.0 255.255.255.0 summary-only"  ]
int_conf =  [
                "int e1/0", "ip address 32.19.86.6 255.255.255.252","no shut",
                "int e1/1", "ip address 17.17.17.1 255.255.255.252","no shut" ]
rprint(net_connect.send_config_set(bgp_comms)+"\n")
rprint(net_connect.send_config_set(int_conf)+"\n")
net_connect.save_config()



#Configuring BGP on R_3:
net_connect=ConnectHandler(**R_3)
net_connect.enable()
bgp_comms = [
                "router bgp 65000",
                "neighbor 1.1.1.1 remote-as 65000",
                "neighbor 1.1.1.1 update-source lo0", ]
rprint(net_connect.send_config_set(bgp_comms))
net_connect.save_config()

net_connect.disconnect()
