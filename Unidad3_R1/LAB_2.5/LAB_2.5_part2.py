'''
    Autor: Arredondo Rangel Christian Geovanni 
    Fecha: 11/12/2023
    Descripcion: LAB_2.5_part2
'''

import json
import requests
from netmiko import ConnectHandler
requests.packages.urllib3.disable_warnings()
#Build the request components

api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"

headers = {
            "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }
basicauth = ("developer", "C1sco12345")

#Create a Python dictionary variable yangConfig 
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback100",
        "description": "WHATEVER100",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "100.100.100.100",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

#Send the PUT request.

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

# Definir la variable ios_device para la conexión SSH
ios_device = {
    'device_type': 'cisco_ios',
    'ip': '10.10.20.48',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22,
    'verbose': True,
}

# Conectar al dispositivo IOS y verificar la eliminación de la interfaz Loopback100
with ConnectHandler(**ios_device) as sshCli:
    output = sshCli.send_command("show ip interface brief | include Loopback100")
    if 'Loopback100' in output:
        print("Loopback100 encontrada")
        # Comando para eliminar la interfaz Loopback100
        cmd_delete_interface = "configure terminal\nno interface Loopback100\nend"
        output_delete = sshCli.send_config_set(cmd_delete_interface)
        print("Loopback100 eliminada exitosamente")
    else:
        print("No encontrada")
