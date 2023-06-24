

from netmiko import ConnectHandler

R1_HUB=  {
            "device_type": "cisco_ios",
            "host": "10.1.1.6",
            "username": "Automation",
            "password": "cisco123",
            "secret": "cisco123"
         }

R1_LAN=  {
            "device_type": "cisco_ios",
            "host": "192.168.99.1",
            "username": "Automation",
            "password": "cisco123",
            "secret": "cisco123" 
         }

firewall={
            "device_type": "cisco_ios",
            "host": "10.1.1.1",
            "username": "Automation",
            "password": "cisco123",
            "secret": "cisco123"
        }

R1_Edge={
            "device_type": "cisco_ios",
            "host": "10.1.1.10",
            "username": "Automation",
            "password": "cisco123",
            "secret": "cisco123",
        }
            

spokes= [{
            "device_type":"cisco_ios",
            "host":"172.31.1.10",
            "username":"Automation",
            "password":"cisco123",
            "secret":"cisco123"
        },
        {
            "device_type":"cisco_ios",
            "host":"172.31.1.20",
            "username":"Automation",
            "password":"cisco123",
            "secret":"cisco123"  
        },

        {
            "device_type":"cisco_ios",
            "host":"172.31.1.30",
            "username":"Automation",
            "password":"cisco123",
            "secret":"cisco123"
        }, 

        {
            "device_type":"cisco_ios",
            "host":"172.31.1.40",
            "username":"Automation",
            "password":"cisco123",
            "secret":"cisco123"
        }]