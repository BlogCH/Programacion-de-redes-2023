'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 4.5.1.22

'''
from datetime import datetime

# Crear un objeto datetime para el 4 de noviembre de 2020 a las 14:53:00
fecha_hora = datetime(2020, 11, 4, 14, 53, 0)

# Imprimir resultados usando strftime con diferentes formatos
print(f"Fecha y hora en formato ISO: {fecha_hora.strftime('%Y/%m/%d %H:%M:%S')}")
print(f"Fecha y hora en formato personalizado: {fecha_hora.strftime('%y/%B/%d %H:%M:%S %p')}")
print(f"Fecha y hora en formato abreviado: {fecha_hora.strftime('%a, %Y %b %d')}")
print(f"Fecha y hora en formato completo: {fecha_hora.strftime('%A, %Y %B %d')}")
print(f"Día de la semana: {fecha_hora.strftime('%w')}")
print(f"Día del año: {fecha_hora.strftime('%j')}")
print(f"Número de semana en el año: {fecha_hora.strftime('%U')}")

