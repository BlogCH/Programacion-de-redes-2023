'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 4.6.1.14 RESUMEN DE SECCIÓN
'''

#Ejercicio 1
#¿Cuál es el resultado del siguiente fragmento de código?
import calendar
print(calendar.weekheader(1))

#Ejercicio 2
#¿Cuál es el resultado del siguiente fragmento de código?
import calendar  

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")