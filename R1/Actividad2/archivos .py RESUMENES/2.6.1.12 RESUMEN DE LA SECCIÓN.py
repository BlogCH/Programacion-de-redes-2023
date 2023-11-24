'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 2.6.1.12 RESUMEN DE LA SECCIÓN
'''
#Ejercicio 1
#¿Cuál es el resultado esperado del siguiente código?
try:
    print("Tratemos de hacer esto")
    print("#"[2])
    print("¡Tuvimos éxito!")
except:
    print("Hemos fallado")
print("Hemos terminado")

#Ejercicio 2
#¿Cuál es el resultado esperado del siguiente código?
try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("cero")
except IndexingError:
    print("índice")
except:
    print("algo")