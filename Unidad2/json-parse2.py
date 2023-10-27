'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/10/2023
    Descripcion: json-parse 2

'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Ocote"
dest = "San Miguel de allende"
key = "pKVy3jdkPgzKEvy1wuf7mDxwyCHC4ADR"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
#Codificar para manejar el error distinto a 0
else:
    print("API Status: " + str(json_status) + " = Tienes un error, Verifica tu code.")