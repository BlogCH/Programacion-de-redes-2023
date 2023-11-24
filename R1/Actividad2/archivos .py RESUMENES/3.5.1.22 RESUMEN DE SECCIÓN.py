'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 3.5.1.22 RESUMEN DE SECCIÓN
'''
# 1. Método __str__()

class Mouse:
    def __init__(self, name):
        self.my_name = name

    def __str__(self):
        return self.my_name

the_mouse = Mouse('mickey')
print(the_mouse)  # Imprime "mickey".

# 2. Función issubclass()

class Mouse:
    pass

class LabMouse(Mouse):
    pass

print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Imprime "False True"

# 3. Función isinstance()

class Mouse:
    pass

class LabMouse(Mouse):
    pass

mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Imprime "True False".

# 4. Operador is

class Mouse:
    pass

mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)  # Imprime "False True".

# 5. Función super()

class Mouse:
    def __str__(self):
        return "Mouse"

class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()

doctor_mouse = LabMouse()
print(doctor_mouse)  # Imprime "Laboratory Mouse".

# 6. Herencia de métodos y variables

class Mouse:
    Population = 0

    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hola, mi nombre es " + self.name

class LabMouse(Mouse):
    pass

professor_mouse = LabMouse("Profesor Mouse")
print(professor_mouse, Mouse.Population)  # Imprime "Hola, mi nombre es Profesor Mouse 1"

# 7. Búsqueda de propiedades

# (No hay código directo para este punto, es una explicación).

# 8. Anulación de métodos y variables

class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name

class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name

mus = AncientMouse("Caesar")  # Imprime "Meum nomen est Caesar"
print(mus)
