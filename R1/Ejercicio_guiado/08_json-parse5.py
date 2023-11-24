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
    # Solicitar al usuario el punto de origen
    orig = input("Starting Location (type 'q' or 'quit' to exit): ")
    if orig.lower() == "q" or orig.lower() == "quit":
        break

    # Solicitar al usuario el punto de destino
    dest = input("Destination (type 'q' or 'quit' to exit): ")
    if dest.lower() == "q" or dest.lower() == "quit":
        break

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
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration:   " + json_data["route"]["formattedTime"])
        print("Miles:           " + str(json_data["route"]["distance"]))

        # Convertir millas a kilómetros y redondear a dos decimales
        miles_to_kilometers = round(json_data["route"]["distance"] * 1.60934, 2)
        print("Kilometers:      " + str(miles_to_kilometers))
        
        # Verificar si 'fuelUsed' está presente antes de imprimirlo
        if 'fuelUsed' in json_data["route"]:
            print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
            print("Fuel Used (Ltr): " + str(json_data["route"]["fuelUsed"] * 3.78))  # Convertir a litros
        else:
            print("Fuel Used information not available.")
            
        print("=============================================")
    else:
        # Imprimir un mensaje indicando que la llamada no fue exitosa
        print(f"Error en la solicitud. Código de estado: {json_status}\n")
