'''
    Autor: Arredondo Rangel Christian Geovanni 
    Fecha: 11/12/2023
    Descripcion: LAB_2.7
'''
#PARTE 1
import ncclient

from ncclient import manager
from ncclient.transport.errors import AuthenticationError, SSHError
#PARTE 2
# Configurar los parámetros de conexión
host = "10.10.20.48" 
port = 830  
username = "developer"
password = "C1sco12345"
hostkey_verify = False

try:
    # Intentar establecer la conexión NETCONF
    m = manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=hostkey_verify
    )

    # Si no se lanzó ninguna excepción, la conexión fue exitosa
    print("Conexión NETCONF exitosa!")
    

except AuthenticationError:
    # Manejar error de autenticación
    print("Error")


#PARTE TRES
finally:
    # Cerrar la conexión si se estableció
    if 'm' in locals():
        m.close_session()
print("# Capacidad admitida (modelos YANG):")
for capability in m.server_capabilities:
    print(capability)

"Pregunta D"
"¿El modelo Cisco-IOS-XE-cdp YANG es compatible con el dispositivo?"
'''
si, este modelo de router es compatible con el modelo YANG
'''