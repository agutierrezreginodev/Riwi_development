"""
Solicita al usuario que introduzca números enteros positivos uno por uno. Suma los valores
que sean mayores que 5 y múltiplos de 3.
Detén el ciclo cuando el usuario introduzca un número negativo par o cuando se hayan
introducido más de 10 números válidos. Muestra la suma acumulada.
"""

# Contador de números válidos
num_valido = 0
# Sumatoria de números válidos
suma_num_validos = 0

# Condición de cierre de ciclo.
while num_valido < 10:
    # Try utilizado para evitar mensaje de error cuando se ingrese un valor de tipo str.
    try:
        # Recepción de datos por consola
        num = int(input("Ingrese un número: "))
    except ValueError:
        # Mensaje que envía el try al obtener un error. En este caso por ingresar un str en vez de un int.
        print("Por favor ingrese un valor numérico.")
        continue
    # Condicional de número válido
    if num > 5 and num % 3 == 0:
        # Adición de números validos a la variable sumatoria 'sum_num_validos'.
        suma_num_validos += num
        # Conteo de números válidos.
        num_valido += 1
    # Condición de cierre de ciclo, que exista un número negativo par.
    elif num < 0 and num % 2 == 0:
        break
    elif num > 0:
        # Conteo de número válido.
        num_valido += 1
    else:
        continue

# Se imprimen los resultados de la sumatoria.
print(f"La suma acumulada de los números mayores que 5 y múltiplos de 3 es ---> {suma_num_validos}.")

