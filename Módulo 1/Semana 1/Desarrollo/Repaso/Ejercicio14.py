"""
Suma de números hasta ingresar 0
Pide al usuario números y súmalos.
El programa debe detenerse cuando el usuario ingrese 0 y mostrar la suma total.
"""

sum = 0

while True:
    num = int(input("Digite un número: "))

    if num != 0:
        sum += num
    else:
        break

print(f"La suma de los números ingresados es: {sum}")