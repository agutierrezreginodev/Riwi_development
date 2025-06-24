"""
Verificar si un número es positivo, negativo o cero
Pide al usuario un número y muestra si es positivo, negativo o cero.
"""

num = float(input("Digite un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")