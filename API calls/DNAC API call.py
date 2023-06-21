
#Making an API call to the Cisco DNAC using the requests function

import requests                                                                              #The requests module is used.
from rich import print as rprint                                                             #The rich library module is used to structure the output into a more readable JSON format.

requests.packages.urllib3.disable_warnings()                                                 #disable warnings from SSL/TLS certificates

url_1="https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

USER= "devnetuser"
PASS= "Cisco123!"
headers={
         "Accept": "application/json"
        }
response=requests.post(url_1, auth=(USER,PASS),headers=headers, verify=False).json()        #The .json() extension outputs the response as a JSON object (Python dictionary)
output=(response["Token"])                                                                  #Getting the dictionary value of the "Token" key.
headers.update({"X-Auth-Token": output})                                                    #Updating the headers dictionary with the Token value with the key as "X-Auth-Token".


url_2="https://sandboxdnac.cisco.com/dna/intent/api/v1/device-health"
rprint(requests.get(url_2, auth=(USER, PASS), headers=headers, verify=False).json())