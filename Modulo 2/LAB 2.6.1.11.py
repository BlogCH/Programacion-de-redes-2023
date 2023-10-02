'''
    Autor: Christian Geovanni Arredondo Rangel 
    Descripcion: LAB 2.6.1.11
    Fecha: 02/10/2023
'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Calcula las horas
total_hours = hour + dura // 60

# Calcula los minutos 
total_minutes = mins + dura % 60

# Ajusta las horas si los minutos superan 59
if total_minutes >= 60:
    total_hours += 1
    total_minutes -= 60

# Asegura que las horas estén en el rango de 0 a 23
total_hours %= 24

# Imprime el resultado en formato de hora (HH:MM)
print(f"{total_hours:02d}:{total_minutes:02d}")
