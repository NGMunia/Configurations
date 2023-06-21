
#Making an API GET request to a cisco IOSXE sandbox

import requests
from rich import print as rprint
requests.packages.urllib3.disable_warnings()  # Disables SSL certificate warnings

USER = "developer"
PASS = "lastorangerestoreball8876"

url="https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/native/interface/Loopback"

headers =   {    
                "accept": "application/yang-data+json"            
            } 
rprint(requests.get(url, auth=(USER,PASS), headers=headers, verify=False).json())
