"""
Conteo de números pares en un rango
Pide dos números al usuario (inicio y fin) y cuenta cuántos números pares hay entre ellos usando for y if.
"""

num1 = int(input("Digite número 1: "))
num2 = int(input("Digite número 2: "))

lista_pares = []

cont = 0

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        lista_pares.append(i)
        cont += 1

print(f"Entre {num1} y {num2} hay {cont} números pares")
print(lista_pares)