'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 4.3.1.17
'''
class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            contenido = file.readlines()

            if not contenido:
                raise FileEmpty("El archivo está vacío.")

            # Inicializar un diccionario para almacenar los puntos de los estudiantes
            puntos_por_estudiante = {}

            # Procesar cada línea del archivo
            for linea in contenido:
                try:
                    # Dividir la línea en nombre, apellido y puntos
                    nombre, apellido, puntos_str = linea.strip().split()

                    # Convertir puntos a un número flotante
                    puntos = float(puntos_str)

                    # Actualizar los puntos para el estudiante en el diccionario
                    puntos_por_estudiante[(nombre, apellido)] = puntos_por_estudiante.get((nombre, apellido), 0) + puntos

                except ValueError:
                    raise WrongLine(f"Línea incorrecta en el archivo: {linea}")

    except FileNotFoundError:
        raise StudentsDataException(f"El archivo {nombre_archivo} no existe.")
    
    return puntos_por_estudiante


def imprimir_reporte(puntos_por_estudiante):
    # Imprimir un informe ordenado por nombre y apellido
    for estudiante, puntos in sorted(puntos_por_estudiante.items()):
        nombre_completo = " ".join(estudiante)
        print(f"{nombre_completo.ljust(20)} {puntos}")


def main():
    try:
        # Pedir al usuario el nombre del archivo del profesor Jekyll
        nombre_archivo = input("Ingrese el nombre del archivo del profesor Jekyll: ")

        # Procesar el archivo y obtener la suma de puntos por estudiante
        puntos_por_estudiante = procesar_archivo(nombre_archivo)

        # Imprimir el informe
        imprimir_reporte(puntos_por_estudiante)

    except StudentsDataException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
