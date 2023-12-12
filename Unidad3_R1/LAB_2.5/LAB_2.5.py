'''
    Autor: Arredondo Rangel Christian Geovanni 
    Fecha: 11/12/2023
    Descripcion: LAB_2.5
'''
import json
import requests
requests.packages.urllib3.disable_warnings()

#Build the request components.
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json", 
             "Content-type":"application/yang-data+json"
           } 
basicauth = ("developer", "C1sco12345")

#Send the request.
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

#Create a new variable called response_json
response_json = resp.json()

print(response_json)

#To prettify the output, use the json.dumps() function with the “indent” parameter:
print(json.dumps(response_json, indent=4))