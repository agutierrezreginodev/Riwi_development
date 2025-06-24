"""
Contador de positivos
Plantea un programa que permita ingresar 10 números y cuente cuántos de ellos son mayores que cero.
"""

cont = 0

print("A continuación ingrese 10 números")

for i in range(10):
    num = int(input(f"Digite un número {i + 1}: "))
    if num > 0:
        cont += 1

print(f"{cont} de los números ingresados son mayores que cero")
