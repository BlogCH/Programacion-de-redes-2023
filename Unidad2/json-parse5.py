'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/10/2023
    Descripcion: Invocando REST API MapQuest

'''


import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    print("Hasta luego")
    
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "pKVy3jdkPgzKEvy1wuf7mDxwyCHC4ADR"

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration:   " + json_data["route"]["formattedTime"])
        
        # Convertir millas a kilómetros
        miles = json_data["route"]["distance"]
        kilometers = miles * 1.60934
        
        print("Kilometers:      " + str(kilometers))
        #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("Latitude:        " + str(json_data["route"]["locations"][0]["latLng"]["lat"]))
        print("Longitude:       " + str(json_data["route"]["locations"][0]["latLng"]["lng"]))
        print("Route Type:      " + json_data["route"]["options"]["routeType"])
        print("=============================================")