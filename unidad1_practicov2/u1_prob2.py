'''
    Autor: CHristian Geovanni Arredondo Rangel 
    Descripcion:u1_prob2.py
    Fecha:02/10/2023
'''
# Lista de asignaturas
asignaturas = [
    "Probabilidad y Estadistica",
    "Electrónica para IDC Fisica",
    "Conexión de redes WAN",
    "Administracion de servidores I",
    "Programacion de Redes",
    "Inglés IV"
]

# Creamos una lista de las calificaciones de cada asignatura 
notas = {}

# Solicita las calificaciones 
for asignatura in asignaturas:
    nota = float(input(f"Ingresa tu calificacion en {asignatura} en la unidad 1: "))
    notas[asignatura] = nota

# Mostrar las notas
print("\nnotas:")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota:.2f}")