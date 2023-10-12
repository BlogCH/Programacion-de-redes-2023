'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.4.1.13
'''
# Paso 1: Crea una lista vacía llamada beatles.
beatles = []

# Paso 2: mplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best
nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]
for miembro in nuevos_miembros:
    beatles.append(miembro)

# Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
del beatles[3]  # Stu Sutcliffe
del beatles[3]  # Pete Best

# Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
beatles.insert(0, "Ringo Starr")

# Imprime la lista de Beatles.
print("Los Beatles:", beatles)

# Probando la longitud de la lista
print("Número de miembros en los Beatles:", len(beatles))
