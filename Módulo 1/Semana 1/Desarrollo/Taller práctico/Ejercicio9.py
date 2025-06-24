"""
Suma de Dígitos
● Escribe un algoritmo que sume todos los dígitos de un número ingresado por
el usuario (por ejemplo, si el usuario ingresa 123, la suma sería 1 + 2 + 3 = 6).
"""

num = int(input("Digite un número: "))

str_num = str(num)

sum = 0

for i in str_num:
    sum += int(i)

print(f"La suma de los digitos del número ingresado es {sum}")

