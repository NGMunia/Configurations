from netmiko import ConnectHandler
#Configuring BGP

#A5000
from  Device_list import A5000
net_connect=ConnectHandler(**A5000)
net_connect.enable()
int_comms=["int e1/0", "ip address 72.73.74.9 255.255.255.252","no shut"]
bgp_comms=["router bgp 5000",
           "neighbor 2.2.2.2 remote-as 5000",
           "neighbor 2.2.2.2 update-source lo0",
           "network 72.73.74.8 mask 255.255.255.252"]
output=net_connect.send_config_set(int_comms)
print(output)
output=net_connect.send_config_set(bgp_comms)
print(output)
print("\n")


#B5000
from Device_list import B5000
net_connect=ConnectHandler(**B5000)
net_connect.enable()
bgp_comms=["router bgp 5000",
           "neighbor 1.1.1.1 remote-as 5000",
           "neighbor 1.1.1.1 update-source lo0",
           "neighbor 1.1.1.1 route-reflector-client",
           "neighbor 3.3.3.3 remote-as 5000",
           "neighbor 3.3.3.3 update-source lo0",
           "neighbor 3.3.3.3 route-reflector-client"]
output=net_connect.send_config_set(bgp_comms)
print(output)
print("\n")


#C5000
from Device_list import C5000
net_connect=ConnectHandler(**C5000)
net_connect.enable()
int_comms=["int e1/0", "ip address 72.73.74.1 255.255.255.252","no shut",
           "int e1/1", "ip address 72.73.74.5 255.255.255.252","no shut"]
bgp_comms=["router bgp 5000",
           "neighbor 2.2.2.2 remote-as 5000",
           "neighbor 2.2.2.2 update-source lo0",
           "neighbor 2.2.2.2 next-hop-self",
           "neighbor 72.73.74.2 remote-as 4000",
           "network 72.73.74.0 mask 255.255.255.252",
           "aggregate-address 72.73.74.0 255.255.255.0 summary-only"]
output=net_connect.send_config_set(int_comms)
print(output)
output=net_connect.send_config_set(bgp_comms)
print(output)
