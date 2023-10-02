'''
    Autor: Christian Geovanni Arredondo Rangel
    Descripcion: LAB 2.6.1.9
    Fecha 02/10/2023
'''
# Ingresa un valor flotante para la variable a aquí
a = float(input("Ingresa un valor flotante para a: "))

# Ingresa un valor flotante para la variable b aquí
b = float(input("Ingresa un valor flotante para b: "))

# Realiza la suma y muestra el resultado
suma = a + b
print("La suma de a y b es:", suma)

# Realiza la resta y muestra el resultado
resta = a - b
print("La resta de a y b es:", resta)

# Realiza la multiplicación y muestra el resultado
multiplicacion = a * b
print("El producto de a y b es:", multiplicacion)

# Realiza la división y muestra el resultado (no te preocupes por la división entre cero)
if b != 0:
    division = a / b
    print("La división de a por b es:", division)
else:
    print("No es posible dividir entre cero.")

print("\n¡Eso es todo, amigos!")
