'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.2.1.6
'''
import time
# Escribe un bucle for que cuente hasta cinco.
for i in range(1,6):
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    print(i, "Mississippi")
    # Cuerpo del bucle - usar: time.sleep (1)
    time.sleep(1)

# Escribe una función de impresión con el mensaje final.
def mensaje_final():
    print("¡Listos o no, ahí voy!")
    
mensaje_final()