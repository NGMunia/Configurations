
#Making an API GET request to a cisco IOSXE sandbox

import requests
from rich import print as rprint

#Disables SSL certificate warnings
requests.packages.urllib3.disable_warnings()  

USER    = "developer"
PASS    = "lastorangerestoreball8876"

url     = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/native/interface/Loopback"

headers =   {    
                "accept": "application/yang-data+json"            
            } 
rprint(requests.get(url, auth=(USER,PASS), headers=headers, verify=False).json())
