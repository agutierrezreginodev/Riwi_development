"""
Dada una lista de productos categorizados:
categorias = ["ropa", "electro", “error1”, "alimento", "otros", "electro", "ropa", "error",
"ropa", "Electro", "ALIMENTO", “error2”, “aeronauticos”]
• Crea un conteo por categoría (ropa, electro, alimento, otros) sin distinguir
mayúsculas/minúsculas.
• Ignora elementos inválidos (los que contienen la palabra error) usando continue.
• Muestra el total de elementos de la lista excluyendo el elemento error.
"""

# Lista de categorías.
categorias = ["ropa", "electro", "error1", "alimento", "otros", "electro", "ropa", "error", "ropa", "Electro", "ALIMENTO", "error2", "aeronauticos"]
# Contadores de categorías en la lista.
cont_ropa = 0
cont_electro = 0
cont_alimento = 0
cont_otros = 0

# Se recorre la lista de categorías para comparar valores.
for categoria in categorias:
    # Si categoría es 'ropa' cuenta uno.
    if categoria.lower() == "ropa":
        cont_ropa += 1
    # Si categoría es 'electro' cuenta uno.
    elif categoria.lower() == "electro":
        cont_electro += 1
    # Si categoría es 'alimento' cuenta uno.
    elif categoria.lower() == "alimento":
        cont_alimento += 1
    # Si categoría es 'otros' cuenta uno.
    elif categoria.lower() != "ropa" or categoria.lower() != "electro" or categoria.lower() != "alimento":
        # Si la palabra 'error' se encuentra en la categoría, se ignora para el conteo.
        if 'error' in categoria:
            continue
        cont_otros += 1

# Se recorre la lista de categorías para comparar valores.
for categoria in categorias:
    # Verifica si la palabra 'error' se encuentra en alguna categoría.
    if 'error' in categoria:
        # La categorías que incluyen 'error', se remueven de la lista.
        categorias.remove(categoria)

# Se imprimen los resultados del conteo de items resultantes de la lista y los conteos por categoría.
print(f"Total de elementos de la lista excluyendo el elemento error ---> {len(categorias)}")
print(f"ropa ---> {cont_ropa}")
print(f"electro ---> {cont_electro}")
print(f"alimento ---> {cont_alimento}")
print(f"otros ---> {cont_otros}")
# Se imprime la lista en pantalla.
print(categorias)
        
        

