'''
Autor: Christian Geovanni Arredondo Rangel
Descripción:Escribir un programa que lea un entero 
positivo, n, introducido por el usuario y después muestre en pantalla 
la suma de todos los enteros desde 1 hasta n. La suma de los n primeros 
enteros positivos puede ser calculada de la siguiente forma:
Fecha: 25/09/2023

'''
n= int(input("Ingresa un numero: "))
suma= n*(n+1)/2
print("El resultado es: ",suma)