'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 3.5.1.23 RESUMEN DE SECCIÓN
'''

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " dice: ¡Guau!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, corderito!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, intruso!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")


# Ejercicio 1
print(rocky)
print(luna)

# Ejercicio 2
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

# Ejercicio 3
print(luna is luna, rocky is luna)
print(rocky.kennel)

# Ejercicio 4
class LowlandDog(SheepDog):
    def __str__(self):
        """
        Retorna una representación en cadena del perro de tierras bajas.

        Returns:
        - str: La representación en cadena del perro de tierras bajas.
        """
        return "¡Guau! ¡No me gustan las montañas!"

# Crear una instancia de LowlandDog
lowland_dog = LowlandDog("SomeBreed")

# Probar el nuevo método __str__()
print(lowland_dog)