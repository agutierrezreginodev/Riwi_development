"""
Contador de intentos
Diseña un programa donde el usuario debe adivinar un número secreto entre 1 y 10. 
Limítale a un máximo de 5 intentos usando while.
"""

import random

cont = 1
winner_num = random.randint(1,10)
num_intentos = 5

print("Adivine un número del 1 al 10")

while cont <= num_intentos:
    user_num = int(input(f"Intento {cont} \nDigite un número: "))
    if user_num == winner_num:
        print("Has adivinado. ¡Enhorabuena!")
        break
    elif num_intentos > cont:
        print("Intente de nuevo")
        cont += 1
        continue
    else:
        break

print(f"No te quedan intentos. \nEl número ganador era {winner_num}")
    