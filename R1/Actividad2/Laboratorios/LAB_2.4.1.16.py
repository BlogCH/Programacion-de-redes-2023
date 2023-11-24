'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 2.4.1.16
'''
def display_siete_segmentos(numero):
    # Patrones de los diez dígitos en siete segmentos
    patrones = [
        ["###", "# #", "# #", "# #", "###"],
        ["  #", "  #", "  #", "  #", "  #"],
        ["###", "  #", "###", "#  ", "###"],
        ["###", "  #", "###", "  #", "###"],
        ["# #", "# #", "###", "  #", "  #"],
        ["###", "#  ", "###", "  #", "###"],
        ["###", "#  ", "###", "# #", "###"],
        ["###", "  #", "  #", "  #", "  #"],
        ["###", "# #", "###", "# #", "###"],
        ["###", "# #", "###", "  #", "###"]
    ]

    # Convertir el número a una lista de dígitos
    digitos = [int(digito) for digito in str(numero)]

    # Imprimir cada línea del display de siete segmentos
    for i in range(5):
        for digito in digitos:
            print(patrones[digito][i], end="   ")
        print()

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número no negativo: "))

# Mostrar el display de siete segmentos para el número ingresado
display_siete_segmentos(numero)
