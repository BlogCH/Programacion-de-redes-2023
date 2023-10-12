'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.2.1.15
'''
c0 = int(input("Ingresa un numero: "))
#Contador se llamara pasos 
pasos = 0 

# c0 tiene que ser diferente a 1 
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 *c0 + 1
    print(c0)  
    pasos += 1

print("pasos =", pasos)