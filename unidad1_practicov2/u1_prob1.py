'''
    Autor: Christian Geovanni Arredondo Rangel 
    Descripcion: No de lista impar El tremendo SAT
    Fecha:02/10/2023
'''

# Solicitar cantidad 
cantidad = float(input("Ingresa la cantidad: $"))

# Calcular el ISR segun los datos dados.
if cantidad <= 0:
    print("La cantidad debe ser mayor que cero")
elif cantidad < 10000:
    isr = cantidad* 0.05
elif cantidad < 20000:
    isr = cantidad* 0.15
elif cantidad < 35000:
    isr = cantidad * 0.20
elif cantidad < 60000:
    isr = cantidad* 0.30
else:
    isr = cantidad * 0.45

# Mostrar el impuesto calculado
if cantidad > 0:
    print(f"El impuesto sobre la renta (ISR)es: ${isr:.2f}")
