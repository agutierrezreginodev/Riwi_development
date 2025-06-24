"""
Cuenta regresiva personalizada
Solicita al usuario un número inicial y muestra una cuenta regresiva hasta llegar a 0 usando for con range(inicio, -1, -1).
"""

num = int(input("Digite un número para la cuenta regresiva: "))

for i in range(num, -1, -1):
    print(i)