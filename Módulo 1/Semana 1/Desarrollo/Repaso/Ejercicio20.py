"""
Factorial de un número
Pide al usuario un número y calcula su factorial usando un ciclo para.
"""

num = int(input("Digite un número: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")

