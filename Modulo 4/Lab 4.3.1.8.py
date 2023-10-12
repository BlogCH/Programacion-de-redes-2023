'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 4.3.1.8
'''
def is_year_leap(year):
    
    # Tu código del LABORATORIO 4.3.1.6
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    
    # Tu código del LABORATORIO 4.3.1.7.
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Comprueba si el año es bisiesto y ajusta febrero si es necesario.
    if is_year_leap(year) and month == 2:
        return 29
    return days_per_month[month - 1]  # Resta 1 para obtener el índice correcto.

def day_of_year(year, month, day):
 
    # Escribe tu código nuevo aquí.
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    # Calcula el día del año.
    day_count = day
    for m in range(1, month):
        day_count += days_in_month(year, m)
    return day_count

print(day_of_year(2000, 12, 31))
