'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 2.3.1.17 RESUMEN DE LA SECCIÓN
'''
#Ejercicio 1
#¿Cuál es el resultado esperado del siguiente código?
for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

print('\n')
#Ejercicio 2
#¿Cuál es el resultado esperado del siguiente código?
s1 = '¿Dónde están las nevadas de antaño?'
s2 = s1.split()
print(s2[-2])

#Ejercicio 3
#¿Cuál es el resultado esperado del siguiente código?
the_list = ['¿Dónde', 'están', 'las', 'nevadas?']
s = '*'.join(the_list)
print(s)

#Ejercicio 4
#¿Cuál es el resultado esperado del siguiente código?
s = 'Es fácil o imposible'
s = s.replace('fácil', 'difícil').replace('im', '')
print(s)