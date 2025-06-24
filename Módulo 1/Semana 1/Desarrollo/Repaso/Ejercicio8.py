"""
Comparación de dos números
Pide al usuario dos números y muestra si son iguales o cuál es mayor.
"""

num1 = int(input("Digite número 1: "))
num2 = int(input("Digite número 2: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Ambos números son iguales.")