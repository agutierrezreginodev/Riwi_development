"""
Contar números positivos
Crea un programa que pida al usuario ingresar 5 números. El programa debe contar cuántos de esos números son positivos.
Resolver primero con while.
Resolver luego con for.
"""

"""
# Utilizando while

cont = 0
cont_positivos = 0

while cont < 5:
    num = int(input("Digite un número: "))
    if num >= 0:
        cont += 1
        cont_positivos +=1
        continue
    else:
        cont += 1
        continue

print(f"De los 5 números ingresados, {cont_positivos} son positivos.")
"""

# Utilizando for

cont = 0

for i in range(5):
    num = int(input("Digite un número: "))
    if num >= 0:
        cont += 1
    
print(f"De los 5 números ingresados, {cont} son positivos.")