"""
Generador de tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10 utilizando for y range().
"""

multi = 0

print("Generador de tabla de multiplicar")
num = int(input("Digite un número: "))

for i in range(1, 11):
    multi = num * i
    print(f"{num} X {i} = {multi}")
