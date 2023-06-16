from netmiko import ConnectHandler

#A4000 
from Device_list import A4000
net_connect=ConnectHandler(**A4000)
net_connect.enable()
int_comms=["int e1/0","ip address 56.57.58.1 255.255.255.252","no shut",
           "int e1/1","ip address 72.73.74.2 255.255.255.252","no shut"]
bgp_comms=["router bgp 4000",
           "neighbor 10.1.1.2 remote-as 4000",
           "neighbor 10.1.1.2 next-hop-self",
           "neighbor 72.73.74.1 remote-as 5000",
           "neighbor 56.57.58.2 remote-as 3000",
           "network 56.57.58.0 mask 255.255.255.252",
           "aggregate-address 56.57.58.0 255.255.255.0 summary-only"]
print(net_connect.send_config_set(bgp_comms)+"\n")
print(net_connect.send_config_set(int_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()


#B4000 (Route-reflector)
from Device_list import B4000
net_connect=ConnectHandler(**B4000)
net_connect.enable()
bgp_comms=["router bgp 4000",
           "neighbor 10.1.1.1 remote-as 4000",
           "neighbor 10.1.1.1 route-reflector-client",
           "neighbor 10.1.1.6 remote-as 4000",
           "neighbor 10.1.1.6 route-reflector-client"]
print(net_connect.send_config_set(bgp_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()



#C4000
from Device_list import C4000
net_connect=ConnectHandler(**C4000)
net_connect.enable()
int_comms=["int e1/0","ip address 44.67.28.2 255.255.255.252","no shut",
           "int e1/1","ip address 59.60.61.1 255.255.255.252","no shut"]
bgp_comms=["router bgp 4000",
           "neighbor 10.1.1.5 remote-as 4000",
           "neighbor 10.1.1.5 next-hop-self",
           "neighbor 44.67.28.1 remote-as 3000",
           "network 59.60.61.0 mask 255.255.255.252",
           "aggregate-address 56.57.58.0 255.255.255.0 summary-only"]
print(net_connect.send_config_set(bgp_comms)+"\n")
print(net_connect.send_config_set(int_comms)+"\n")
net_connect.save_config()
net_connect.disconnect()

