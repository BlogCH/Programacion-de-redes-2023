'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.2.1.14
'''
blocks = int(input("Ingresa el número de bloques:"))

altura = 0
bloques_utilizados = 0

while bloques_utilizados + altura + 1 <= blocks:
    altura += 1
    bloques_utilizados += altura

print("La altura de la pirámide es:", altura)
