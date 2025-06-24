"""
Mayor de tres números
Pide al usuario tres números y muestra cuál es el mayor de ellos.
"""

num1 = int(input("Ingrese número 1: "))
num2 = int(input("Ingrese número 2: "))
num3 = int(input("Ingrese número 3: "))

if num1 > num2 and num1 > num3:
    print(f"El número mayor es {num1}")
elif num2 > num3 and num2 > num1:
    print(f"El número mayor es {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El número mayor es {num3}")