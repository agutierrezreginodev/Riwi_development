"""
Sumar números hasta cancelar
Permite al usuario ingresar números de manera indefinida. 
Usa un while True que termina si el usuario escribe “salir”, acumulando los números ingresados.
"""

sum = 0

while True:
    num = int(input("Digite un número: "))
    sum += num
    
    opcion_seguir = input("Desea seguir ingresando números? (s/n): ")

    if opcion_seguir == "s":
        continue
    elif opcion_seguir == "n":
        break

print(f"la sumatoria de los números ingresados es {sum}")