
#COMMON CONFIGURATIONS

from netmiko import ConnectHandler
from rich import print as rprint
from Device_List import SW, R1, R2



#SNMP
def snmp_config():
    """This function will configure SNMP on the Network devices.
This forms part of Data traffic collection and analysis"""
    rprint('\n'f'[cyan]{snmp_config.__doc__}[/cyan]'+'\n')
    for routers in R1,R2,SW:
        net_connect=ConnectHandler(**routers)
        net_connect.enable()
        commands=["ip access-list standard SNMP",
              "permit host 192.168.99.254",
              "snmp-server community xyz_routers ro SNMP",
              "snmp-server system-shutdown",
              "snmp-server enable traps config",
              "snmp-server host 192.168.255.254 traps version 2c xyz_routers"]
        rprint(net_connect.send_config_set(commands)+"\n")
        net_connect.save_config()
    
    
    
#NTP
def ntp_config():
    """This function will configure NTP on the devices"""
    rprint('\n'f'[cyan]{ntp_config.__doc__}[/cyan]'+'\n')
    for devices in R1,SW,R2:
        net_connect=ConnectHandler(**devices)
        net_connect.enable()
        ntp_server= input(f'{devices.get("host")}: input NTP server IP address: ')
        ntp_commands=["ip domain lookup",
                      "ip name-server 8.8.8.8",
                      "ntp server "+ntp_server,
                      "ntp update-calendar",
                      "clock timezone GMT +3"]
        rprint(net_connect.send_config_set(ntp_commands)+"\n")
        net_connect.save_config()
    


#EEM applets
def EEM_config():
    """This funtion will configure EEM applet to the router.
Automatic backup of start-up config to TFTP server will occur every Monday to Saturday at 12:30 PM"""
    rprint('\n'f'[cyan]{EEM_config.__doc__}[/cyan]'+'\n')
    for devices in R1,R2,SW:
        net_connect=ConnectHandler(**devices)
        net_connect.enable()
        filename = input(f'{devices.get("host")}: TFTP filename for this device: ' )
        EEM  = ["event manager environment tftpserver tftp://192.168.99.254/",
                "event manager environment filename "+filename,
                "event manager applet Automatic_backup_weekdays",
                "event timer cron cron-entry \"30 12 * * 1-6\"",
                "action 1.0 cli command \"enable\"",
                "action 1.1 cli command \"debug event manager action cli\"",
                "action 1.2 cli command \"conf t\"",
                "action 1.3 cli command \"file prompt quiet\"",
                "action 1.4 cli command \"do copy start $tftpserver$filename\"",
                "action 1.5 cli command \"no file prompt quiet\"",
                "action 1.6 syslog priority informational msg \"TFTP backup successful\""]
        rprint(net_connect.send_config_set(EEM)+"\n")
        net_connect.save_config()
    


#NETFLOW
def netflow_config():
    """This function will configure NetFlow on the Network devices.
This forms part of Data traffic collection and analysis"""
    rprint('\n'f'[cyan]{netflow_config.__doc__}[/cyan]'+'\n')
    net_connect=ConnectHandler(**R1)
    net_connect.enable()
    netflow =  ["ip flow-export version 9",
                "ip flow-export destination 192.168.99.254 9996",
                "ip flow-cache timeout active 1",
                "ip flow-top-talkers",
                "top 5",
                "sort-by bytes",
                "int e0/1",
                "ip nbar protocol-discovery",
                "ip flow ingress",
                "ip flow egress"]
    rprint(net_connect.send_config_set(netflow)+"\n")
    net_connect.save_config()



#CoPP
def CoPP_config():
    """This function will configure CoPP on the Network devices.
This aims to protect the RP from DOS attacks"""
    rprint('\n'f'[cyan]{CoPP_config.__doc__}[/cyan]'+'\n')
    for routers in R1,R2:
        net_connect=ConnectHandler(**routers)
        net_connect.enable()
        rprint(net_connect.send_config_from_file("C:\\Users\\Munia-virtual\\Desktop\\Scripts\\Configurations\\Project II\\CoPP.txt"))
        net_connect.save_config()



#Syslog
def syslog_conf():
    """This function will configure Syslog on the Network devices."""
    rprint(f'[cyan]{syslog_conf.__doc__}[/cyan]'+'\n')
    for devices in R1,R2,SW:
        net_connect=ConnectHandler(**devices)
        net_connect.enable()
        syslog= ["logging monitor informational",
                 "logging host 192.168.99.254",
                 "logging trap",
                 "service timestamps log datetime localtime year",
                 "service timestamps debug datetime localtime year"]
        rprint(net_connect.send_config_set(syslog)+'\n')
    


