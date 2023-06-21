
import requests
from rich import print as rprint
import json

#Disables SSL certificate warnings
requests.packages.urllib3.disable_warnings()  

USER    = "developer"
PASS    = "lastorangerestoreball8876"

url     = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/native/interface"

headers =   {    
              "accept": "application/yang-data+json",
              "content-type":"application/yang-data+json"            
            } 
data    =   { "Loopback":{
                            "name": 1986,
                            "description": "Configured by Munia using RESTCONF",
                            "ip": {"address": {"primary": {"address": "10.19.86.1", "mask": "255.255.255.255"}}}
                         }
            } 
#The json.dumps() function is used to convert a Python object (in this case, the data dictionary) to a JSON-formatted string
data=json.dumps(data)

rprint("Status code: "+str(requests.post(url, auth=(USER,PASS), data=data, headers=headers,verify=False)))
