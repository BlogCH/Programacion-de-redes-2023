'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 3.6.1.9 RESUMEN DE SECCIÓN
'''
#Ejercicio 1
#¿Cuál es el resultado esperado del siguiente código?
import math
try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("ok")
    
#Ejercicio 2
#¿Cuál es el resultado esperado del siguiente código?
import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("ok")
finally:
    print("fin")

#Ejercicio 3
#¿Cuál es el resultado esperado del siguiente código?

import math

class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Advertencia enemiga", "Alerta roja", "Alta disponibilidad")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')