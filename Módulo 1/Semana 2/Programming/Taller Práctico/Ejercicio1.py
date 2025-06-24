"""
Dada la siguiente lista:
numeros = [5, -3, 12, 0, 15, 8, 22, -10, 33, 11, 19, -7]
Cuenta cuántos números positivos mayores que 10 hay y cuántos son negativos
múltiplos de 3.
Muestra ambos totales. Al final, calcula el porcentaje que representa cada grupo respecto
al total de elementos.
"""

# Lista de números
numeros = [5, -3, 12, 0, 15, 8, 22, -10, 33, 11, 19, -7]

#Contador números positivos mayores que 10.
cont_positivos_10 = 0
#Contador números negativos múltiplos de 3.
cont_negativos_3 = 0

# Recorremos la lista de números para realizar comparaciones y sumar a los contadores.
for numero in numeros:
    # Conteo de número positivos mayores a 10.
    if numero > 10:
        cont_positivos_10 += 1
    # Conteo de números negativos múltiplos de 3.
    elif numero < 0 and numero % 3 == 0:
        cont_negativos_3 += 1

# Porcentaje = Números positivos mayores a 10 dividido cantidad de números de la lista, y el resultado multiplicado por cien.
porcentaje_positivos = (cont_positivos_10/len(numeros)) * 100
# Porcentaje = Números negativos y múltiplos de 3 dividido cantidad de números de la lista, y el resultado multiplicado por cien.
porcentaje_negativos = (cont_negativos_3/len(numeros)) * 100

# Se imprime en consola los resultados.
print(f"Números positivos mayores que 10 ---> {cont_positivos_10} \nPorcentaje en comparación al total ---> {porcentaje_positivos:.2f}%\n")
print(f"Negativos múltiplos de 3 ---> {cont_negativos_3} \nPorcentaje en comparación al total ---> {porcentaje_negativos:.2f}%")