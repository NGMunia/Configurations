#Libraries
from netmiko import ConnectHandler
from rich import print as rprint
from Device_list import core_sw, SW1,SW2,SW3,SW4,R1_Edge,FW_1

#COnfiguring Core-Switch:
def core():
    """Configuring CORE SWITCH
    - Vlans and Trunking
    - Inter-VLAN routing
    - Access-Control lists
    - OSPF summarization
    - NTP"""
    rprint(f'[yellow]{core.__doc__}[/yellow]'+'\n')

    net_connect=ConnectHandler(**core_sw)
    net_connect.enable()
    for v in range (10,40,10):
        name     = input(f'VLAN '+str(v)+' name: ')
        vlans    = [
                    'vlan '+str(v), 
                    'name '+name ]
        vlan_int = [
                    'int vlan '+str(v), 
                    'ip address 10.1.'+str(v)+'.1 255.255.255.0',
                    'no shut',
                    'ip access-group access_acl in',
                    'ip ospf 1 area 123',
                    'ip helper-address 10.1.40.254' ]
        acls     = [
                    'ip access-list extended vty_acl',
                    'deny tcp 10.1.0.0 0.0.31.255 any eq 22 log',
                    'permit ip any any' ]
        ntp      = [
                    'ntp server 192.168.1.6',
                    'ntp update-calendar',
                    'clock timezone GMT +3',
                    'service timestamps log datetime localtime year',
                    'service timestamps debug datetime localtime year']
        ospf     = ['router ospf 1',
                    'area 123 range 10.1.0.0 255.255.192.0']
        
        for commands in vlans, vlan_int, acls, ntp, ospf:
            print(net_connect.send_config_set(commands)+'\n')
        net_connect.save_config()
core()     



#Configuring Access switches
def access_sw():
    """Configuring Access Switches:
    - VLANs
    - Access and Trunk ports
    - NTP"""
    rprint(f'[yellow]{access_sw.__doc__}[/yellow]'+'\n')

    for access_switches in SW1,SW2,SW3,SW4:
        net_connect=ConnectHandler(**access_switches)
        net_connect.enable()
        vlan_list  = input(f'SW {access_switches.get("ip")} VLANs: ')
        for access_ports in range(0,4):
            intf   = [ 
                        "int e0/"+str(access_ports),
                        "switchport mode access",
                        "switchport access vlan "+vlan_list ]
            print(net_connect.send_config_set(intf)+'\n')
        ntp        = [
                        'ntp server 10.1.40.1',
                        'ntp update-calendar',
                        'clock timezone GMT +3',
                        'service timestamps log datetime localtime year',
                        'service timestamps debug datetime localtime year']
        print(net_connect.send_config_set(ntp)+'\n')
        net_connect.save_config()
access_sw()



#Configuring FW_1:
def firewall_conf():
    """Configuring Firewall Router:
    - ZBF"""
    rprint(f'[yellow]{firewall_conf.__doc__}[/yellow]')
    
    net_connect=ConnectHandler(**FW_1)
    net_connect.enable()

    zbf_config = [
                    'ip access-list extended In_Out_acl',
                    'permit tcp any any eq 443',
                    'permit tcp any any eq 80',
                    'permit icmp any any',
                    'permit udp any any',
                    'ip access-list extended Out_In_acl',
                    'permit ip host 192.168.1.6 any',
                    'class-map type inspect In_Out_class',
                    'match access-group name In_Out_acl',
                    'class-map type inspect Out_In_class',
                    'match access-group name Out_In_acl',
                    'policy-map type inspect In_Out_Policy',
                    'class In_Out_class',
                    'inspect',
                    'policy-map type inspect Out_In_Policy',
                    'class Out_In_class',
                    'inspect',
                    'zone security Inside',
                    'zone security Outside',
                    'zone-pair security In_Out_zone source Inside destination Outside',
                    'service-policy type inspect In_Out_class',
                    'zone-pair security Out_In_zone source Outside destination Inside',
                    'service-policy type inspect Out_In_class',
                    'int e0/0',
                    'zone-member security Inside',
                    'int e0/1',
                    'zone-member security Outside' ]
    print(net_connect.send_config_set(zbf_config)+'\n')
    net_connect.save_config()
firewall_conf()
    


#Configuring R1
def R1_conf():
    """Configuring the Edge Router
    - NAT"""
    rprint(f'[yellow]{R1_conf.__doc__}[/yellow]'+'\n')
    
    net_connect=ConnectHandler(**R1_Edge)
    net_connect.enable()

    nat_conf = [
                'ip access-list standard nat_acl',
                'permit 10.1.0.0 0.0.31.255',
                'int e0/1',
                'ip address dhcp',
                'ip nat outside',
                'no shut',
                'int e0/0',
                'ip nat inside',
                'ip nat inside source list nat_acl int e0/1 overload' ]
    print(net_connect.send_config_set(nat_conf)+'\n')
    net_connect.save_config()
R1_conf()

    

def common_configs():
    """This Functon will configure the following:
    - SNMP
    - Syslog
    - NTP
    - EEM"""   
    rprint(f'[yellow]{common_configs.__doc__}[/yellow]')

    for devices in R1_Edge, FW_1:
        net_connect=ConnectHandler(**devices)
        net_connect.enable()
        snmp        =   [
                          'ip access-list standard snmp_acl',
                          'permit host 10.1.40.254',
                          'snmp-server community devices_snmp ro snmp_acl',
                          'snmp-server enable traps config',
                          'snmp-server host 10.1.40.254 traps version 2c devices_snmp']
        syslog      =   [
                          'logging monitor informational',
                          'logging host 10.1.40.254',
                          'logging trap']
        server_ip   = input(f'Host {devices.get("ip")} NTP server IP: ') 
        ntp         =   [
                          'ip domain-lookup',
                          'ip name-server 8.8.8.8',
                          'ntp server '+server_ip,
                          'ntp update-calendar',
                          'clock timezone GMT +3',
                          'service timestamps log datetime localtime year',
                          'service timestamps debug datetime localtime year']
        filename    = input(f'Host {devices.get("ip")} TFTP filename: ')
        eem_applet  =   [
                          'event manager environment tftpserver tftp://10.1.40.254/',
                          'event manager environment filename '+filename,
                          'event manager applet Automatic_Backup_Config',
                          'event timer cron cron-entry "30 11 * * 1-6"',
                          'action 1.0 cli command "enable"',
                          'action 1.1 cli command "debug event manager action cli"',
                          'action 1.2 cli command "conf t"',
                          'action 1.3 cli command "file prompt quiet"',
                          'action 1.4 cli command "do copy start $tftpserver$filename"',
                          'action 1.5 cli command "no file prompt quiet"',
                          'action 1.6 syslog priority informational msg "TFTP backup successful"']
        for commands in snmp, syslog, ntp, eem_applet:
            print(net_connect.send_config_set(commands)+'\n')
            net_connect.save_config()      
common_configs()
    


    



