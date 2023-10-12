'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.4.1.6
'''
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: Solicita al usuario reemplazar el número del medio con un número ingresado por el usuario.
numero_ingresado = int(input("Ingresa un número entero para reemplazar el número central: "))
hat_list[2] = numero_ingresado  # Reemplaza el número del medio.

# Paso 2: Elimina el último elemento de la lista.
del hat_list[-1]

# Paso 3: Imprime la longitud de la lista existente.
print("La longitud de la lista es:", len(hat_list))

print(hat_list)
