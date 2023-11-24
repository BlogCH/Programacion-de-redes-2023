'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha:10/10/2023
    Descripción: Plantilla 
'''
import requests
import time

# Diccionario para almacenar los nombres de los animes y sus cantidades agrupados por la primera letra
animes_por_letra = {}

while True:
    respuesta = input("¿Quieres obtener información sobre algún anime? (s/n): ")

    if respuesta.lower() == 's':
        url = 'https://api.jikan.moe/v4/top/anime'
        data = requests.get(url)

        if data.status_code == 200:
            data = data.json()
            for anime in data['data']:
                title = anime['title']
                first_letter = title[0].upper()  # Obtener la primera letra y convertirla a mayúscula

                # Agregar el anime al diccionario
                if first_letter not in animes_por_letra:
                    animes_por_letra[first_letter] = {'nombres': [title], 'cantidad': 1}
                else:
                    animes_por_letra[first_letter]['nombres'].append(title)
                    animes_por_letra[first_letter]['cantidad'] += 1

            # Mostrar todos los nombres de los animes disponibles
            print("Nombres de todos los animes disponibles:")
            for letra, animes in animes_por_letra.items():
                for anime in animes['nombres']:
                    print(anime)
            print(f"\nCantidad total de animes: {sum(animes['cantidad'] for animes in animes_por_letra.values())}")
        else:
            print(f"Error en la solicitud. Código de estado: {data.status_code}")
    elif respuesta.lower() == 'n':
        print("No quieres obtener información sobre algún anime. ¡Hasta luego!")
        break
    else:
        print("Respuesta no válida. Por favor, responde 's' para sí o 'n' para no.")

    # Esperar durante un cierto período antes de realizar la próxima solicitud
    time.sleep(2)
