"""
Verificar si un número es par o impar
Pide al usuario un número y muestra si es par o impar.
"""

num = int(input("Digite un número: "))

if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")