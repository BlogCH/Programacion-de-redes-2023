'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/10/2023
    Descripcion: json-parse 3

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

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")