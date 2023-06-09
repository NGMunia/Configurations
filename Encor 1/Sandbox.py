

from netmiko import ConnectHandler
from Devices import R1_LAN

for vpn in R1_LAN:
    netconnect=ConnectHandler(**vpn)
    netconnect.enable()
    output=netconnect.send_command("show ntp status")
    print(output)


