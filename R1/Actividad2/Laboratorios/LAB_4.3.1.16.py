'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 4.3.1.16
'''
def contar_letras(archivo):
    # Inicializar un diccionario para almacenar recuentos de letras
    recuentos = {}

    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leer el contenido del archivo
            contenido = file.read()

            # Iterar sobre cada caracter del contenido
            for caracter in contenido:
                # Verificar si el caracter es una letra latina
                if caracter.isalpha():
                    # Convertir el caracter a minúscula para contar sin distinguir entre mayúsculas y minúsculas
                    caracter = caracter.lower()

                    # Incrementar el contador de la letra en el diccionario
                    recuentos[caracter] = recuentos.get(caracter, 0) + 1

    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    return recuentos

def imprimir_histograma(recuentos):
    # Ordenar el diccionario por frecuencia de caracteres
    sorted_recuentos = sorted(recuentos.items(), key=lambda x: x[1], reverse=True)

    # Imprimir el histograma ordenado
    for letra, frecuencia in sorted_recuentos:
        print(f"{letra} -> {frecuencia}")

def guardar_histograma(archivo, recuentos):
    # Crear el nombre del archivo de salida con extensión '.hist'
    archivo_salida = archivo.split('.')[0] + '.hist'

    try:
        # Abrir el archivo en modo escritura
        with open(archivo_salida, 'w') as file:
            # Escribir el histograma ordenado en el archivo
            for letra, frecuencia in sorted(recuentos.items(), key=lambda x: x[1], reverse=True):
                file.write(f"{letra} -> {frecuencia}\n")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

def main():
    # Pedir al usuario el nombre del archivo de entrada
    archivo = input("Ingrese el nombre del archivo: ")

    # Contar las letras en el archivo
    recuentos = contar_letras(archivo)

    # Imprimir el histograma ordenado
    imprimir_histograma(recuentos)

    # Guardar el histograma en un archivo con extensión '.hist'
    guardar_histograma(archivo, recuentos)

if __name__ == "__main__":
    main()
