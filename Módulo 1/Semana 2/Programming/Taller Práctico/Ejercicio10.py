"""
Escribe un programa que reciba una palabra e indique si es o no un palíndromo.
Solo puedes usar un único ciclo, ya sea for o while, para comparar letra por letra.

Una palabra palíndroma es aquella que se lee igual de izquierda a derecha que de derecha
a izquierda.
Por ejemplo:
"reconocer" es un palíndromo porque al invertirla se obtiene "reconocer".

Condiciones: Solo se podrá utilizar for o while, cadenas, condicionales, lógica booleana, no
se puede utilizar funciones de Python que inviertan cadenas.
"""

# Se ingresa la palabra por consola.
palabra = input("Ingrese una palabra: ")
# Lista para añadir los caracteres en orden contrario.
palabra_caracteres = []

# Se recorre la palabra de la última letra a la primera.
for caracter in palabra[::-1]:
    # Se añade cada caracter a la lista.
    palabra_caracteres.append(caracter)

# Se utiliza el metodo join() para juntar todos los items de la lista mediante un separador en un solo string.
palabra_al_reves = "".join(palabra_caracteres)

# Comparamos si la palabra es palíndroma.
if palabra == palabra_al_reves:
    print("Es palíndroma")
else:
    print("No es palíndroma")