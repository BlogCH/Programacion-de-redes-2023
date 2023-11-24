'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 4.2.1.12 RESUMEN DE SECCIÓN
'''
#Actividad 1
#¿Cómo se codifica el valor del argumento modo de la función open() si se va a crear un nuevo archivo de texto?

print("La respuesta AC1 es wt o w")

#Ejercicio 2
#¿Cuál es el significado del valor representado por errno.EACESS?
print("￼Permiso denegado: no se permite acceder al contenido del archivo.")

#Ejercicio 3
#¿Cuál es la salida esperada del siguiente código, asumiendo que el archivo llamado file no existe?
import errno

try:
    stream = open("file", "rb")
    print("existe")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("ausente")
    else:
        print("desconocido")