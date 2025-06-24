"""
Calculadora de factorial
Pide un número al usuario y calcula su factorial usando un ciclo for.
"""

num = int(input("Digite un número: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")
