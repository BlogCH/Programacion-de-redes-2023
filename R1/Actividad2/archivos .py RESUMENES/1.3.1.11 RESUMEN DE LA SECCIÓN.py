'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: 1.3.1.11 RESUMEN DE LA SECCIÓN
    
'''
#Ejercicio 1
#Deseas evitar que el usuario de tu módulo ejecute tu código como un script ordinario. ¿Cómo lograrías tal efecto?
import sys

if __name__ == "__main__":
    print ("¡No hagas eso!")
    sys.exit()
    
#Ejercicio 2
#Algunos paquetes adicionales y necesarios se almacenan dentro del directorio D:\Python\Project\Modules. Escribe
# un código asegurándote de que Python recorra el directorio para encontrar todos los módulos solicitados.
import sys

# ¡Toma en cuenta las diagonales invertidas dobles!
sys.path.append("D:\\Python\\Project\\Modules")