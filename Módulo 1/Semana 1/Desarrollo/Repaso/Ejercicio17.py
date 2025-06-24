"""
Tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10 usando un ciclo para.
"""

print("Tablas de multiplicar")
num = int(input("De que número deseas saber su tabla? "))

for i in range(1, 11):
    multi = num * i
    print(f"{num} X {i} = {multi}")