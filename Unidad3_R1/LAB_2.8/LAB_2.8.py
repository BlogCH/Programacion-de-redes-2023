'''
    Autor: Arredondo Rangel Christian Geovanni 
    Fecha: 11/12/2023
    Descripcion: LAB_2.8
'''
from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="10.10.20.48",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
)

# Obtén la configuración en ejecución sin filtro
netconf_reply = m.get_config(source="running")
print(netconf_reply)
'''
# Intenta obtener la configuración específica usando el filtro en la operación get
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get(filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''