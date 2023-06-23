
from netmiko import ConnectHandler
from rich import print as rprint
from Device_List import SW, R1, R2
from global_Configurations import netflow_config, ntp_config, snmp_config, CoPP_config,EEM_config


    
#Configuring the Switch:
rprint("[cyan]==========CONFIGURING THE SWITCH==========[/cyan]\n")
net_connect=ConnectHandler(**SW)
net_connect.enable()    
vlans_conf = [
              "vlan 100","name Data_VLAN",
              "int g0/0", "switchport access vlan 100",
              "int g1/0", "switchport mode trunk","switchport trunk allowed vlan add 100"
             ]    
ports   =    [
              "int range g0/2-3",
              "switchport access vlan 99",
              "switchport port-security",
              "switchport port-security mac-address sticky",
              "switchport port-security maximum 2",
              "switchport port-security violation restrict"
             ] 
   
spantree=    ["int range g0/0-3", "spanning-tree portfast", "spanning-tree bpduguard enable"]   
 
vacl    =    [
              "ip access-list extended VLAN_99_acl",
              "permit ip any 192.168.99.0 0.0.0.255",
              "vlan access-map VLAN_100_VACL 10",
              "match ip address VLAN_99_acl",
              "action drop log",
              "vlan access-map VLAN_100_VACL 20",
              "action forward",
              "exit",
              "vlan filter VLAN_100_VACL vlan-list 100"
             ]
commands=[vlans_conf,ports,spantree,vacl]
for commands in commands:
    rprint(net_connect.send_config_set(commands)+"\n")
    net_connect.save_config()
    

#Configuring R1:
#    - DHCP
#    - QoS
net_connect=ConnectHandler(**R1)
net_connect.enable()

dhcp= ["ip dhcp excluded-address 192.168.100.1 192.168.100.10",
       "ip dhcp pool VLAN_100",
       "network 192.168.100.0 255.255.255.0",
       "default-router 192.168.100.1",
       "dns-server 208.67.222.123",
       "lease 0 2"]
QoS = ["class-map match-any Scavenger_class",
       "match protocol netflix",
       "match protocol bittorrent",
       "class-map match-any Social_media_class",
       "match protocol facebook",
       "match protocol twitter",
       "match protocol instagram",
       "policy-map Internet_policy",
       "class Scavenger_class",
       "drop",
       "class Social_media_class",
       "police 128K conform-action transmit exceed-action drop",
       "set dscp cs1",
       "class class-default",
       "set dscp default",
       "fair-queue",
       "interface e0/1", "service-policy output Internet_policy"
       ]
commands=[dhcp,QoS]
for commands in commands:
    rprint(net_connect.send_config_set(commands))
    net_connect.save_config()


#Configuring R2:
#    - NAT
#    - QoS
#    - Time-based ACL
net_connect=ConnectHandler(**R2)
net_connect.enable()
QoS = [
       "class-map match-all Social_media_class",
       "match ip dscp cs1",
       "policy-map Internet_policy",
       "class Social_media_class",
       "set dscp cs1" ]
nat= ["int e0/0", 
      "ip nat inside", 
      "int e0/1",
      "ip nat outside",
      "ip address dhcp",
      "no shut",
      "ip access-list standard nat_acl",
      "permit 192.168.96.0 0.0.7.255",
      "ip nat inside source list nat_acl interface e0/1 overload",
      "ip route 0.0.0.0 0.0.0.0 192.168.122.1",
      "router ospf 1",
      "default-information originate"]  
commands=[QoS,nat]  
for commands in commands:
    rprint(net_connect.send_config_set(commands))
    net_connect.save_config()
   

#Global configurations:
netflow_config()
snmp_config()
CoPP_config()
EEM_config()
ntp_config()
