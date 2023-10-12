'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.2.1.3
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numbers = int(input("Ingresa el numero secreto: "))

while numbers != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numbers = int(input("Vuelve a intentarlo: "))

print("¡Bien hecho, muggle! Eres libre ahora!")