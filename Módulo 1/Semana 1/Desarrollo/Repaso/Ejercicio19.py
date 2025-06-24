"""
Mostrar los primeros N números pares
Pide al usuario un número N y muestra los primeros N números pares.
"""

num = int(input("Digite un número: "))

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)

