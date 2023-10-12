'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.2.1.10
'''

user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()  # Esto convierte la palabra a mayúsculas

for palabra in user_word:
    if palabra in "AEIOU":
        continue  
    print(palabra)