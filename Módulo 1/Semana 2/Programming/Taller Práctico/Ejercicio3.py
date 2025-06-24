"""
Recorre los números del 1 al 100.
• Suma los múltiplos de 5.
• Usa continue para omitir los demás.
• Muestra cuántos se sumaron y cuál fue el total.
"""

# Sumatoria de números múltiplos de 5.
sum_multiplos_5 = 0
# Contador de números múltiplos de 5.
cont_multiplos_5 = 0

for i in range(1, 101):
    # Condición de que i sea múltiplo de 5.
    if i % 5 == 0:
        # Adición de números múltiplos a la variable sumatoria 'sum_multiplos_5'.
        sum_multiplos_5 += i
        # Conteo de números múltiplos.
        cont_multiplos_5 += 1
    else:
        # En caso tal no cumpla con ninguna condición, no se realiza ningún tratamiento.
        continue

# Se imprimen los resultados del conteo y de la sumatoria de los múltiplos de 5.
print(f"Se sumaron {cont_multiplos_5} números múltiplos de 5. \nTotal de la suma fue ---> {sum_multiplos_5}")