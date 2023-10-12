'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 11/10/2023
    Descripcion: Lab 3.1.1.11
'''
income = float(input("Introduce el ingreso anual:"))

exencion_fiscal = 85528
impuesto_base = 14839.2

if income <= exencion_fiscal:
    tax = (income * 0.18) - 556.02
else:
    tax = impuesto_base + (income - exencion_fiscal) * 0.32

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
