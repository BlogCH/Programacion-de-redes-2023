'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 3.3.1.9 RESUMEN DE SECCIÓN
'''
#Ejercicio 1
#¿Cuáles de las propiedades de la clase Python son variables de instancia y cuáles 
# son variables de clase? ¿Cuáles de ellos son privados?

class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False

#population y victims son variables de clase, mientras que length y __venomous son
# variables de instancia (esta última también es privada).

#Ejercicio 2
#Vas a negar la propiedad __venomous del objeto version_2, ignorando el hecho de que la propiedad es 
# privada. ¿Cómo vas a hacer esto?

version_2 = Python()
print("Respuesta del ejercicio 2")