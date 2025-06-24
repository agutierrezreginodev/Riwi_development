"""
Imprime los números del 1 al 100, omitiendo aquellos que:
• Contengan el dígito 7, y
• Sean múltiplos de 3.
(Pista: Convierte el número a str y usa continue si cumple ambas condiciones)
"""
# Lista de números omitidos debido a las condiciones mencionadas.
num_omitidos = []
# Ciclo iterativo para imprimir los números del 1 al 100
for i in range(1, 101):
    # Conversión del número a tipo string.
    num = str(i)
    # Se verifica si el caracter '7' se encuentra en el string y si el número es múltiplo de 3.
    if '7' in num and i % 3 == 0:
        # Se añaden los números omitidos a la lista creada.
        num_omitidos.append(num)
        # Se vuelve a iniciar el ciclo.
        continue
    else:
        # Si el número no cumple con las condiciones, se imprime en pantalla.
        print(num)

# Se imprimen también en pantalla los números omitidos.
print(f"Los números omitidos fueron: \n{num_omitidos}")