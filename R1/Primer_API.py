'''
    Autor: Chistian Geovanni Arredondo Rangel
    Descripcion: Primer API 
    Fecha: 16/11/2023
'''

import requests

url_love_calculator = "https://love-calculator.p.rapidapi.com/getPercentage"
headers_love_calculator = {
    "X-RapidAPI-Key": "8bd4e3adf1msh747fa2a313d9a48p15429ejsn61287345c545",
    "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

while True:
    sname = input("Ingresa el nombre de la primera persona ('salir' para terminar): ")
    if sname.lower() == 'salir':
        break

    fname = input("Ingresa el nombre de la segunda persona: ")

    querystring_love_calculator = {"sname": sname, "fname": fname}

    try:
        response_love_calculator = requests.get(url_love_calculator, headers=headers_love_calculator, params=querystring_love_calculator)
        response_love_calculator.raise_for_status()

        if 'percentage' in response_love_calculator.json():
            love_percentage = response_love_calculator.json()['percentage']
            print(f"Porcentaje de amor entre {sname} y {fname}: {love_percentage}%")
            print(response_love_calculator.json())
        else:
            print("Error: No se pudo obtener el porcentaje de amor.")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
