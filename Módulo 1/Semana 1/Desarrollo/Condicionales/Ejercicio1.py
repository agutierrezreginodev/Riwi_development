"""
Determinar signo y paridad
Dado un número entero proporcionado por el usuario, determina primero si es positivo, negativo o cero. Si el número no es cero, establece además si es par o impar.
"""

num = int(input("Digite un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

if num != 0:
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")