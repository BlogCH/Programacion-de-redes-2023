'''
    Autor: Chistian Geovanni Arredondo Rangel
    Descripcion: Segunda API 
    Fecha: 16/11/2023
'''

import requests

url_urban_dictionary = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
term_to_define = input("Ingresa el término a definir en Urban Dictionary ('salir' para terminar): ")

while term_to_define.lower() != 'salir':
    querystring_urban_dictionary = {"term": term_to_define}
    headers_urban_dictionary = {
        "X-RapidAPI-Key": "8bd4e3adf1msh747fa2a313d9a48p15429ejsn61287345c545",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }

    try:
        response_urban_dictionary = requests.get(url_urban_dictionary, headers=headers_urban_dictionary, params=querystring_urban_dictionary)
        response_urban_dictionary.raise_for_status()

        urban_data = response_urban_dictionary.json()

        if 'list' in urban_data:
            if urban_data['list']:
                first_definition = urban_data['list'][0].get('definition', 'No disponible')
                print(f"Definición de '{term_to_define}': {first_definition}")
            else:
                print(f"No se encontró una definición para '{term_to_define}'.")
        else:
            print("Error: No se pudo obtener la definición.")

    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

    term_to_define = input("Ingresa otro término a definir en Urban Dictionary ('salir' para terminar): ")
