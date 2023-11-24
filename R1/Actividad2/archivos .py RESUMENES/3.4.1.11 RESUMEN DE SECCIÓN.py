'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 3.4.1.11 RESUMEN DE SECCIÓN
'''
'''
#Ejercicio 1
#La declaración de la clase Snake se muestra a continuación.
#Enriquece la clase con un método llamado increment(), el cual incrementa en 1 la propiedad victims.

class Snake:
    def __init__(self):
        self.victims = 0
#######################################################################################
 class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1

#Ejercicio 2
#Redefine el constructur de la clase Snake para que tenga un parámetro que inicialice el 
# campo victims con un valor pasado al objeto durante la construcción.
class Snake:
    def __init__(self, victims):
        self.victims = victims	
        
'''
#Ejercicio 3
#¿Puedes predecir el resultado del siguiente código?
class Snake:
    pass

class Python(Snake):
    pass

print(Python.__name__, 'es una', Snake.__name__)
print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__)


