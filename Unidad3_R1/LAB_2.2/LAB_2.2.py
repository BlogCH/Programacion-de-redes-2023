'''
    Autor: Arrredondo Rangel Christian Geovanni 
    Descripcion: LAB_2.2
    Fecha 10/12/2023
'''
#PARTE 1
import netmiko
from netmiko import ConnectHandler

#PARTE 2
sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.10.20.48',
    port = 22,
    username = 'developer',
    password = 'C1sco12345'
)
#PARTE 3
output = sshCli.send_command('show ip int brief')
print("show ip int brief: :\n",output)
#PARTE 4
config_commands = [
    'int loopback 1', 
    'ip address 2.2.2.2 255.255.255.0', 
    'description WHATEVER'
                  ]
config_commands_loopback2 = [
    'interface loopback 2',
    'ip address 2.2.2.2 255.255.255.0', 
    'description ip_igual'
]
output = sshCli.send_config_set(config_commands)