"""
Solicita un número n al usuario. Busca los primeros 10 números primos menores que n,
usando una combinación de for y while.
• Si n < 10, muestra un mensaje de error y termina.
• Muestra la lista de primos encontrados.
"""

primos = []

num = int(input("Digite un número: "))

for n in range(2, num + 1):
    es_primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(n)

print(primos)