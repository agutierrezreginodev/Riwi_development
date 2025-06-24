"""
Suma de los primeros N números naturales
Pide al usuario un número N y muestra la suma de los números del 1 al N.
"""

num = int(input("Digite un número: "))
sum = 0

for i in range(1, num + 1):
    sum += i

print(f"La suma de los números del 1 al {num} es {sum}.")