'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 4.3.1.18 RESUMEN DE SECCIÓN
'''

#Ejercicio 1
#¿Qué se espera del método readlines() cuando el stream está asociado con un archivo vacío?
print("￼Una lista vacía (una lista de longitud cero).")

#Ejercicio 2
#¿Qué se pretende hacer con el siguiente código?
#for line in open("file", "rt"):
 #   for char in line:
  #      if char.lower() not in "aeiouy ":
   #         print(char, end='')
print("Copia el contenido del archivo file hacia la consola, ignorando las vocales.")

#Ejercico 3
#Vas a procesar un mapa de bits almacenado en un archivo llamado image.png y quieres leer su contenido como un todo en una variable bytearray llamada image. Agrega una línea al siguiente código para lograr este objetivo.

try:
    stream = open("image.png", "rb")
    # Inserta una línea aquí.
    stream.close()
except IOError:
    print("fallido")
else:
    print("exitoso")

