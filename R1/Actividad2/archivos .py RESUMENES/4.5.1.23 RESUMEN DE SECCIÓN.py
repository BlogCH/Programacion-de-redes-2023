'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 4.5.1.23 RESUMEN DE SECCIÓN
'''
#Ejercicio 1
#¿Cuál es el resultado del siguiente fragmento de código?
from datetime import time

t = time(14, 39)
print(t.strftime("%H:%M:%S"))

#Ejercicio 1
#¿Cuál es el resultado del siguiente fragmento de código?
from datetime import datetime

dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)
print(dt1 - dt2)

