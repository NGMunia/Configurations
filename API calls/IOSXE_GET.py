
#Making an API GET request to a cisco IOSXE sandbox

import requests
from rich import print as rprint

#Disables SSL certificate warnings
requests.packages.urllib3.disable_warnings()  

USER    = "admin"
PASS    = "C1sco12345"

url     = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/native/interface/Loopback"

headers =   {    
                "accept": "application/yang-data+json"            
            } 
rprint(requests.get(url, auth=(USER,PASS), headers=headers, verify=False).json())
