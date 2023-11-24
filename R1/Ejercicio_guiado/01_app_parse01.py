'''
    Autor: Christian Geovanni Arredondo Rangel
    Descripion: Parsing JSON with a Python Application 
    Fecha: 20/Noviembre/2023
'''
import urllib.parse
import requests

# Paso 1: Construir la URL para la solicitud de la API de MapQuest

# URL principal de la API
main_api = "https://www.mapquestapi.com/directions/v2/route"

# Parámetros para especificar el punto de origen y destino
orig = "Nueva+York,NY"
dest = "Los+Ángeles,CA"

# Clave de API de MapQuest
key = "Z76dPONA5SfqjzyOnRAIu26ZqPZ0c0Ht"

# Construir la URL completa
url = f"{main_api}?key={key}&from={orig}&to={dest}"

response = requests.get(url)
json_data = response.json()

# Imprimir la representación JSON de la respuesta
print("Datos JSON devueltos:")
print(json_data)