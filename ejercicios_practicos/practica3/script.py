'''
	nombre: Christian Geovanni Arredondo Rangel
	Asignatura:Programacion de redes.
	Descripción del problema: 
'''
# Dentro del script crear una lista vacía llamada lstnombres.
lstnombres=[] 
# Solicitar al usuario cinco nombres y agregarlos a la lista.
for i in range(5):
    nombres = input(f"Dime quien son 5 de tus mejores amig@s {i + 1}: ")
    lstnombres.append(nombres)

#Dentro del script crear una lista vacía llamada lstedades
lstedades = []
#Solicitar al usuario las edades y agregarlas a la lista.
for i in range(5):
    edad = input(f"Ingrese la edad de {lstnombres[i]}: ")
    lstedades.append(edad)
    
#Crear un diccionario con nombres como clave y edades como valor.
dicDatos = {}
for i in range(5):
    dicDatos[lstnombres[i]] = lstedades[i]

#Crear una función para mostrar el contenido del diccionario.
def mostrar_diccionario(diccionario):
    for nombre, edad in diccionario.items():
        print(f"Nombre de tu amig@: {nombre} -> edad: {edad}")

#Invocar la función para mostrar el contenido del diccionario.
print("Contenido del diccionario:")
mostrar_diccionario(dicDatos)

#Desplegar la longitud de las listas y el diccionario.
print(f"Longitud de lstnombres: {len(lstnombres)}")
print(f"Longitud de lstedades: {len(lstedades)}")
print(f"Longitud de dicDatos: {len(dicDatos)}")

#Ordenar las claves del diccionario y desplegarlas.
claves_ordenadas = sorted(dicDatos.keys())
print("Claves ordenadas:", claves_ordenadas)

#Crear una función para buscar una clave en el diccionario.
def buscar_clave(diccionario, clave):
    if clave in diccionario:
        return diccionario[clave]
    else:
        return None

#Ejemplo de búsqueda en el diccionario.
clave_buscar = input("Ingrese un nombre para buscar en el diccionario: ")
resultado_busqueda = buscar_clave(dicDatos, clave_buscar)
if resultado_busqueda is not None:
    print(f"{clave_buscar} -> {resultado_busqueda}")
else:
    print(f"{clave_buscar} no encontrado en el diccionario.")
