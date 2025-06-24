"""
Suma de Números
● Escribe un algoritmo que sume todos los números enteros desde 1 hasta un
número ingresado por el usuario.
"""

num = int(input("Digite un número: "))
sum = 0

for i in range(1, num + 1):
    sum += i

print(f"La suma de todos los números desde 1 hasta {num} es: {sum}")