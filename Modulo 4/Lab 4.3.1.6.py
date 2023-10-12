'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 4.3.1.6

'''
def is_year_leap(year):
#
# Escribe tu código aquí.
#

# Comprueba si el año es bisiesto.

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

# Itera a través de los datos de prueba y compara los resultados con los esperados
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    # Imprime el año, la flecha y luego "OK" si es correcto o "Fallido" si no. 
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")