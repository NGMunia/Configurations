
#Making an API GET request to a cisco IOSXE sandbox
import xml
import requests
from rich import print as rprint

#Disables SSL certificate warnings
requests.packages.urllib3.disable_warnings()  

USER    = "admin"
PASS    = "C1sco12345"

url     = "https://sandbox-iosxe-latest-1.cisco.com:830/netconf/data/native"

headers =   {    
                "accept": "application/yang-data+xml"            
            } 
rprint(requests.get(url, auth=(USER,PASS), headers=headers, verify=False))