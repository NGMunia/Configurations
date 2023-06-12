#BGP configuration:
from netmiko import ConnectHandler

#C3000
from Device_list import C3000 #Route reflector 
net_connect=ConnectHandler(**C3000)
net_connect.enable()
bgp_comms=["router bgp 3000",
           "neighbor 1.1.1.1 remote-as 3000",
           "neighbor 1.1.1.1 update-source lo0",
           "neighbor 1.1.1.1 route-reflector-client",
           "neighbor 2.2.2.2 remote-as 3000",
           "neighbor 2.2.2.2 update-source lo0",
           "neighbor 2.2.2.2 route-reflector-client",
           "neighbor 4.4.4.4 remote-as 3000",     
           "neighbor 4.4.4.4 update-source lo0",
           "neighbor 4.4.4.4 route-reflector-client",
           "neighbor 5.5.5.5 remote-as 3000",
           "neighbor 5.5.5.5 update-source lo0",
           "neighbor 5.5.5.5 route-reflector-client"]
ouput=net_connect.send_config_set(bgp_comms)
net_connect.save_config()
net_connect.disconnect()


#A3000
from Device_list import A3000
net_connect=ConnectHandler(**A3000)
net_connect.enable()
bgp_comms=["router bgp 3000",
           "neighbor 3.3.3.3 remote-as 3000",
           "neighbor 3.3.3.3 update-source lo0",
           "neighbor 3.3.3.3 next-hop-self",
           "neighbor 173.128.4.1 remote-as 2000"]
ouput=net_connect.send_config_set(bgp_comms)
net_connect.save_config()
net_connect.disconnect()
print(ouput)
print("\n")



#B3000
from Device_list import B3000
net_connect=ConnectHandler(**B3000)
net_connect.enable()
bgp_comms=["router bgp 3000",
           "neighbor 3.3.3.3 remote-as 3000",
           "neighbor 3.3.3.3 update-source lo0",]
ouput=net_connect.send_config_set(bgp_comms)
net_connect.save_config()
net_connect.disconnect()
print(ouput)
print("\n")


#D3000
from Device_list import D3000
net_connect=ConnectHandler(**D3000)
net_connect.enable()
bgp_comms=["router bgp 3000",
           "neighbor 3.3.3.3 remote-as 3000",
           "neighbor 3.3.3.3 update-source lo0",
           "network 44.67.28.0 mask 255.255.255.252",
           "neighbor 44.67.28.2 remote-as 4000",
           "aggregate-address 44.67.28.0 255.255.255.0 summary-only"]
ouput=net_connect.send_config_set(bgp_comms)
net_connect.save_config()
net_connect.disconnect()
print(ouput)
print("\n")

#E3000
from Device_list import E3000
net_connect=ConnectHandler(**E3000)
net_connect.enable()
bgp_comms=["router bgp 3000",
           "neighbor 3.3.3.3 remote-as 3000",
           "neighbor 3.3.3.3 update-source lo0",
           "neighbor 3.3.3.3 next-hop-self",
           "network 32.19.86.0 mask 255.255.255.252",
           "aggregate-address 32.19.86.0 255.255.255.0 summary-only"]
ouput=net_connect.send_config_set(bgp_comms)
net_connect.save_config()
net_connect.disconnect()
print(ouput)
