"""
Sumatoria hasta alcanzar un mínimo
Solicita al usuario que ingrese números. Sigue sumándolos hasta que la suma sea mayor a 100. Usa un while.
"""

sum = 0

print("Por favor ingrese números, el programa sumará los números ingresado, \ny cuando la suma sea mayor que 100 se detendrá.")

while sum < 100:
    num = int(input("Digite un número: "))
    sum += num

print(f"La suma total es {sum}")