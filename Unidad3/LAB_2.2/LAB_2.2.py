'''
    Autor:Christian Geovanni Arredondo Rangel
    Descripcion: LAB_2.2
    Fecha 27/Noviembre/2023
'''

from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.10.20.48',
    port = 22,
    username = 'developer',
    password = 'C1sco12345'
)

output = sshCli.send_command('show ip int brief')
print("show ip int brief: :\n",output)


#Use netmiko to alter configuration on the device
config_comands =[
    'int loopback 1',
    'ip address 2.2.2.2 255.255.255.0', #Error de tipografia 
    'description WHATEVER'
]
output =sshCli.send_config_set(config_comands)

# Mostrar las interfaces despues de realzar los cambios de direccion a la loopback 1
output = sshCli.send_command('show ip int brief')
print("interfaces despues de realzar los cambios de direccion a la loopback 1\n",output)