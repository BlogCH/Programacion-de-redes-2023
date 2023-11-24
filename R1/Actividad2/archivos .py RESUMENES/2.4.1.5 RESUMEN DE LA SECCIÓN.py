'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 2.4.1.5 RESUMEN DE LA SECCIÓN
'''
#Ejercicio 1
#¿Cuál de las siguientes líneas describe una condición verdadera?
'smith' > 'Smith'
'Smiths' < 'Smith'
'Smith' > '1000'
'11' < '8'
print("El resultado de la activiad 1, es 1, 3 y 4")

#Ejercicio 2
#¿Cuál es el resultado esperado del siguiente código?
s1 = '¿Dónde están las nevadas de antaño?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])

#Ejercicio 3
#¿Cuál es el resultado esperado del siguiente código?
s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)