"""
Dada una lista de palabras:
palabras = ["casa", "ordenador", "mesa", "código123", "sol", "ventilador", "mouse",
"teclado", "pantalla7"]
• Ignora palabras que contengan números (continue).
• Las que tienen más de 6 letras colócalas imprímelas.
• Imprime la cantidad total de palabras que contienen más de 6 letras.
"""

# Lista de palabras.
palabras = ["casa", "ordenador", "mesa", "código123", "sol", "ventilador", "mouse", "teclado", "pantalla7"]
# Contador de palabras con más de seis letras y no contienen números.
cont_palabras = 0

# Recorrido de lista de palabras.
for palabra in palabras:
    # Condición de que la palabra solo contenga letras.
    if palabra.isalpha() == True:
        # Si la palabra tiene mas de seis letras realice...
        if len(palabra) > 6:
            # Imprima la palabra en consola.
            print(palabra)
            # Añada a la cuenta dicha palabra.
            cont_palabras += 1
    else:
        continue

# Imprima los resultados del conteo en pantalla.
print(f"La cantidad de palabras con más de seis letras y no contienen números ---> {cont_palabras}")