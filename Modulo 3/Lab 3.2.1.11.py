'''
Autor : Christian Geovanni Arredondo Rangel
Fecha 11/10/2023
Descriocion: Lab 3.2.1.11
'''
word_without_vowels = ""  # Inicializa la variable para almacenar las letras no consumidas

# Indica al usuario que ingrese una palabra
# y asígnala a la variable user_word.
user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()  # Convierte la palabra a mayúsculas

for palabra in user_word:
    if palabra in "AEIOU":
        continue  
    word_without_vowels += palabra

print(word_without_vowels)