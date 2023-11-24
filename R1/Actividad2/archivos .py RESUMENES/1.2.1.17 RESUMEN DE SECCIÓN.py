'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 1.2.1.17 RESUMEN DE SECCIÓN.
    
'''
#Ejercicio 1
#¿Cuál es el valor esperado de la variable result después de que se ejecuta el siguiente código?

import math
result = math.e == math.exp(1)
print(result)

#Ejercicio 2
#(Completa el enunciado) Establecer la semilla del generador 
# con el mismo valor cada vez que se ejecuta tu programa garantiza que ...

#... los valores pseudoaleatorios emitidos desde el módulo random serán exactamente los mismos.

#Ejercicio 3
#¿Cuál de las funciones del módulo platform utilizarías para determinar el nombre del CPU que corre dentro de tu computadora?

#La función processor()

#Ejercicio 4

#¿Cuál es el resultado esperado del siguiente fragmento de código?
import platform

print(len(platform.python_version_tuple()))

