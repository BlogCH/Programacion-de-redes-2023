'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 2.8.1.4
'''
def ingresar_numero(minimo, maximo):
    while True:
        try:
            entrada = int(input(f'Ingresa un número entre {minimo} y {maximo}: '))
            if minimo <= entrada <= maximo:
                return entrada
            else:
                print(f'Error: el valor no está dentro del rango permitido ({minimo}..{maximo})')
        except ValueError:
            print('Error: entrada incorrecta')

# Ejemplo de uso
try:
    numero_ingresado = ingresar_numero(-10, 10)
    print(f'El número es: {numero_ingresado}')
except KeyboardInterrupt:
    print('\nEntrada de usuario cancelada.')
