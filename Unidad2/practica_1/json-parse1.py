'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/10/2023
    Descripcion:

'''


import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimore"
key = "pKVy3jdkPgzKEvy1wuf7mDxwyCHC4ADR"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data['route']['sessionId'])
#Extrae la distancia y tiempo
print(json_data['route']['distance'])
print(json_data['route']['time'])
#Extrae del primer elemento Legs el campo formattedTime
formatted_time = json_data['route']['legs'][0]['formattedTime']
print(formatted_time)