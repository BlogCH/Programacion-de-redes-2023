'''
    Autor: Christian Geovanni Arredondo Rangel
    Descripion: Parsing JSON with a Python Application 
    Fecha: 20/Noviembre/2023
'''
import requests
import urllib.parse

# URL principal de la API
main_api = "https://www.mapquestapi.com/directions/v2/route"

# Clave de API de MapQuest
key = "Z76dPONA5SfqjzyOnRAIu26ZqPZ0c0Ht"

# Implementar un bucle while para permitir que el usuario realice múltiples solicitudes
while True:
    # Solicitar al usuario el punto de origen y destino
    orig = input("Starting Location: ")
    dest = input("Destination: ")

    # Construir la URL completa con los nuevos valores de origen y destino
    url = f"{main_api}?key={key}&from={orig}&to={dest}"

    # Imprimir la URL construida para que el usuario pueda ver la solicitud exacta realizada por la aplicación
    print("URL: " + url)

    # Realizar la solicitud a la API y obtener los datos JSON
    json_data = requests.get(url).json()

    # Extraer el valor del código de estado de la respuesta JSON
    json_status = json_data["info"]["statuscode"]

    # Verificar si el código de estado es 0, que indica una llamada exitosa
    if json_status == 0:
        # Imprimir un mensaje indicando que la llamada fue exitosa
        print("API Status: " + str(json_status) + " = A successful route call.\n")
    else:
        # Imprimir un mensaje indicando que la llamada no fue exitosa
        print(f"Error en la solicitud. Código de estado: {json_status}\n")
