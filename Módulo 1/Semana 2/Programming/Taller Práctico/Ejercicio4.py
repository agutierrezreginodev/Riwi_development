"""
Verificación y creación de usuarios
Dada la tupla de usuarios:
usuarios_registrados = ("ana", "luis", "maria", "carlos")
Y la lista:
usuarios_nuevos = ["pedro", "ana", "maria", "sofia", "lucas", "Luis"]
recorre ambas estructuras e imprime los nombres de usuario que se repiten
"""

# Tupla usuarios registrados
usuarios_registrados = ("ana", "luis", "maria", "carlos")
# Lista usuarios nuevos
usuarios_nuevos = ["pedro", "ana", "maria", "sofia", "lucas", "Luis"]

# Recorrido de la lista usuarios_nuevos
for usuario_nuevo in usuarios_nuevos:
    # Se verifica si el valor obtenido de la lista se encuentra en la tupla. 
    if usuario_nuevo in usuarios_registrados:
        # Se imprimen los nombres repetidos.
        print(usuario_nuevo)