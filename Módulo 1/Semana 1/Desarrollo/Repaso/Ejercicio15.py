"""
Adivinar un número secreto
Define un número secreto (por ejemplo, 7).
Pide al usuario que adivine el número hasta que lo acierte.
"""

winner_num = 16
user_num = 0

while user_num != winner_num:
    user_num = int(input("Digite un número: "))

    if user_num > winner_num:
        print("Estas por encima del número ganador.")
    elif user_num < winner_num:
        print("Estas por debajo del número ganador.")

print("Felicidades, obtuviste el número ganador.")