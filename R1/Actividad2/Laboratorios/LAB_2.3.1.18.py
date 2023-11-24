'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 2.3.1.18
'''
def mysplit(cadena):
    # Inicializar una lista para almacenar las palabras
    palabras = []

    # Inicializar una variable para construir cada palabra
    palabra_actual = ""

    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        # Verificar si el carácter es un espacio en blanco
        if caracter.isspace():
            # Agregar la palabra actual a la lista si no está vacía
            if palabra_actual:
                palabras.append(palabra_actual)
                palabra_actual = ""
        else:
            # Concatenar el carácter a la palabra actual
            palabra_actual += caracter

    # Agregar la última palabra si no está vacía
    if palabra_actual:
        palabras.append(palabra_actual)

    return palabras

# Ejemplos de uso
print(mysplit("Ser o no ser esa es, la pregunta"))
print(mysplit("Ser o no ser,esa es la preguntla"))
print(mysplit(""))
print(mysplit("abc"))
print(mysplit("   "))  # Prueba con espacios en blanco solamente
