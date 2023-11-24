'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 4.4.1.8
'''
import os

def find(path, target_dir):
    # Obtener la ruta absoluta del directorio de inicio
    abs_path = os.path.abspath(path)

    # Iniciar la búsqueda recursiva
    buscar_directorio(abs_path, target_dir)

def buscar_directorio(current_path, target_dir):
    try:
        # Listar los elementos en el directorio actual
        elementos = os.listdir(current_path)

        for elemento in elementos:
            # Construir la ruta completa del elemento
            elemento_path = os.path.join(current_path, elemento)

            if os.path.isdir(elemento_path):
                # Si es un directorio, realizar búsqueda recursiva
                buscar_directorio(elemento_path, target_dir)
            elif os.path.basename(elemento_path) == target_dir:
                # Si es el directorio objetivo, imprimir la ruta absoluta
                print(os.path.abspath(elemento_path))

    except PermissionError:
        # Ignorar errores de permisos
        pass
    except Exception as e:
        print(f"Error al buscar directorio: {e}")

# Ejemplo de uso
find("./tree", "python")

