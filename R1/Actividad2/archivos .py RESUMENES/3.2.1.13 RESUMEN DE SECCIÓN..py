'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 3.2.1.13 RESUMEN DE SECCIÓN.
'''
#Ejercicio 1
#Suponiendo que hay una clase llamada Snakes, escribe la primera línea de la declaración de clase Python, expresando el hecho de que la nueva clase es en realidad una subclase de Snake.
print("La respuesta es class Python(Snakes):")

#Ejercicio 2
#Algo falta en la siguiente declaración, ¿qué es?

class Snakes
    def __init__():
        self.sound = 'Sssssss'

print("El constructor __init__() carece del parámetro obligatorio (deberíamos llamarlo self para cumplir con los estándares).")

#Ejercicio 3
#Modifica el código para garantizar que la propiedad venomous sea privada.
class Snakes
    def __init__(self):
        self.venomous = True
'''
El código debería verse como sigue:

class Snakes
    def __init__(self):
        self.__venomous = True")
'''