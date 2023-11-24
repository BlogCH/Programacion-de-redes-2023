
import urllib.parse
import requests

# Paso 1: Construir la URL para la solicitud de la API de MapQuest

# URL principal de la API
main_api = "https://www.mapquestapi.com/directions/v2/route"


# Clave de API de MapQuest
key = "Z76dPONA5SfqjzyOnRAIu26ZqPZ0c0Ht"

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
