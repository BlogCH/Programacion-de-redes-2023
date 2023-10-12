'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 11/10/2023
    Descripcion: Lab 3.1.1.12
'''

year = int(input("Ingresa un año: "))

if year < 1582:
    print("No dentro del período del calendario Gregoriano.")
elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Año Bisiesto")
else:
    print("Año Común")
