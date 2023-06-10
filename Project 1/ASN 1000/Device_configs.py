
from netmiko import ConnectHandler

#Configuring BGP:
#A1000
from Device_list import A1000
net_connect=ConnectHandler(**A1000)
net_connect.enable()
bgp_comms=["router bgp 1000",
           "neighbor 2.2.2.2 remote-as 1000",
           "neighbor 2.2.2.2 update-source lo0",
           "neighbor 2.2.2.2 route-reflector-client",
           "neighbor 3.3.3.3 remote-as 1000",
           "neighbor 3.3.3.3 update-source lo0",
           "neighbor 3.3.3.3 route-reflector-client",
           "network 200.165.201.0 mask 255.255.255.252",
           "aggregate-address 200.165.201.0 255.255.255.0 summary-only"]
output=net_connect.send_config_set(bgp_comms)
net_connect.save_config()
net_connect.disconnect()

#B1000    
from Device_list import B1000
net_connect=ConnectHandler(**B1000)
net_connect.enable()
bgp_comms=["router bgp 1000",
           "neighbor 1.1.1.1 remote-as 1000",
           "neighbor 1.1.1.1 update-source lo0",
           "neighbor 1.1.1.1 next-hop-self",
           "neighbor 173.128.1.1 remote-as 2000",
           "neighbor 173.128.1.1 filter-list 10 out"]
commands=["ip as-path access-list 10 permit ^$"]
output=net_connect.send_config_set(bgp_comms)
output=net_connect.send_config_set(commands)
net_connect.save_config()
net_connect.disconnect()

#C1000
from Device_list import C1000
net_connect=ConnectHandler(**C1000)
net_connect.enable()
bgp_comms=["router bgp 1000",
           "neighbor 1.1.1.1 remote-as 1000",
           "neighbor 1.1.1.1 update-source lo0",
           "neighbor 1.1.1.1 next-hop-self",
           "neighbor 173.128.2.1 remote-as 2000",
           "neighbor 173.128.2.1 filter-list 10 out"]
commands=["ip as-path access-list 10 permit ^$"]
output=net_connect.send_config_set(bgp_comms)
output=net_connect.send_config_set(commands)
net_connect.save_config()
net_connect.disconnect()
