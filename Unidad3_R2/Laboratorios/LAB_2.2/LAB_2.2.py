'''
    Autor:Christian Geovanni Arredondo Rangel
    Fecha: 22 Enero 2024
    Descripcion LAB_2.2
'''

import netmiko
from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.10.20.48',
    port = 22,
    username = 'developer',
    password = 'C1sco12345'
)
#Parte 3

output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))

#parte 4


config_commands = [
    'int loopback 1', 
    'ip address 2.2.2.2 255.255.255.0', 
    'description WHATEVER'
                  ] 

output = sshCli.send_config_set(config_commands)


'''
¿Por qué el resultado de “show ip int brief” no incluye la interfaz “loopback1”?
Porque aun no estaba creada la interfaz.
¿Cómo ejecutar y mostrar el resultado del comando “show ip int brief” después de crear las
interfaces loopback?
con la linea output_after_config = sshCli.send_command('show ip int brief') se puede
mostrar el resultado de show ip int brief
Agregue código para crear una nueva interfaz de loopback (loopback2) con la misma
dirección IP que en la interfaz de loopback existente, solo que con una descripción
diferente.
Ejecute el archivo de script Python y verifique los resultados.¿Se creó correctamente la nueva interfaz loopback2?
No, generar un conflicto con las interfaces loopback 1 y 2 por lo que no crea ninguna nueva
interfaz hasta que se cambie a una ip diferente a las demás interfaces existentes.
'''