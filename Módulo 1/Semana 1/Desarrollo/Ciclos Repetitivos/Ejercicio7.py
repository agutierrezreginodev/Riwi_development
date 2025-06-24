"""
Contador de letras 'a'
Solicita una palabra al usuario y cuenta cuántas veces aparece la letra 'a'. Utiliza un for para recorrer la cadena.
"""

palabra = input("Ingrese una palabra: ")

cont = 0

for caracter in palabra:
    if caracter.lower() == "a":
        cont += 1

print(f"La palabra '{palabra} contiene {cont} letras 'a'.")