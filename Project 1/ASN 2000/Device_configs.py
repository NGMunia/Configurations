#BGP configuration:
from netmiko import ConnectHandler

#C2000
from Device_list import C2000 #Route reflector 
net_connect=ConnectHandler(**C2000)
net_connect.enable()
int_comms=["int e1/0","ip address 173.128.4.1 255.255.255.252","no shut"]
bgp_comms=["router bgp 2000",
           "neighbor 1.1.1.1 remote-as 2000",
           "neighbor 1.1.1.1 update-source lo0",
           "neighbor 1.1.1.1 route-reflector-client",
           "neighbor 1.1.1.1 next-hop-self",
           "neighbor 2.2.2.2 remote-as 2000",
           "neighbor 2.2.2.2 update-source lo0",
           "neighbor 2.2.2.2 next-hop-self",
           "neighbor 2.2.2.2 route-reflector-client",
           "neighbor 4.4.4.4 remote-as 2000",
           "neighbor 4.4.4.4 update-source lo0",
           "neighbor 4.4.4.4 route-reflector-client",
           "neighbor 5.5.5.5 remote-as 2000",
           "neighbor 5.5.5.5 update-source lo0",
           "neighbor 5.5.5.5 next-hop-self",
           "neighbor 5.5.5.5 route-reflector-client",
           "neighbor 173.128.4.2 remote-as 3000",
           "network 173.128.4.0 mask 255.255.255.252",
           "aggregate-address 173.128.4.0 255.255.255.0 summary-only"]
print(net_connect.send_config_set(bgp_comms)+"\n")
print(net_connect.send_config_set(int_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()


#A2000
from Device_list import A2000
net_connect=ConnectHandler(**A2000)
net_connect.enable()
bgp_comms=["router bgp 2000",
           "neighbor 3.3.3.3 remote-as 2000",
           "neighbor 3.3.3.3 update-source lo0",
           "neighbor 3.3.3.3 next-hop-self",
           "neighbor 173.128.1.2 remote-as 1000",
           "network 173.128.1.0 mask 255.255.255.252",
           "aggregate-address 173.128.1.0 255.255.255.0 summary-only"]
int_comms=["int e1/0","ip address 173.128.1.1 255.255.255.252","no shut"]
print(net_connect.send_config_set(bgp_comms)+"\n")
print(net_connect.send_config_set(int_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()


#B2000
from Device_list import B2000
net_connect=ConnectHandler(**B2000)
net_connect.enable()
bgp_comms=["router bgp 2000",
           "neighbor 3.3.3.3 remote-as 2000",
           "neighbor 3.3.3.3 update-source lo0",
           "neighbor 3.3.3.3 next-hop-self",
           "neighbor 72.73.74.5 remote-as 5000"]
int_comms=["int e1/0","ip address 72.73.74.6 255.255.255.252","no shut"]
print(net_connect.send_config_set(bgp_comms)+"\n")
print(net_connect.send_config_set(int_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()



#D2000
from Device_list import D2000
net_connect=ConnectHandler(**D2000)
net_connect.enable()
bgp_comms=["router bgp 2000",
           "neighbor 3.3.3.3 remote-as 2000",
           "neighbor 3.3.3.3 update-source lo0",
           "network 173.128.3.0 mask 255.255.255.252",
           "aggregate-address 173.128.3.0 255.255.255.0 summary-only"]
int_comms=["int e1/0","ip address 173.128.3.1 255.255.255.252","no shut"]
print(net_connect.send_config_set(bgp_comms)+"\n")
print(net_connect.send_config_set(int_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()



#E2000
from Device_list import E2000
net_connect=ConnectHandler(**E2000)
net_connect.enable()
bgp_comms=["router bgp 2000",
           "neighbor 3.3.3.3 remote-as 2000",
           "neighbor 3.3.3.3 update-source lo0",
           "neighbor 3.3.3.3 next-hop-self",
           "neighbor 173.128.2.2 remote-as 1000",
           "network 173.128.2.0 mask 255.255.255.252",
           "aggregate-address 173.128.2.0 255.255.255.0 summary-only"]
int_comms=["int e1/0","ip address 172.128.2.1 255.255.255.252","no shut",
           "int e1/1","ip address 173.128.2.5 255.255.255.252","no shut"]
print(net_connect.send_config_set(bgp_comms)+"\n")
print(net_connect.send_config_set(int_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()

