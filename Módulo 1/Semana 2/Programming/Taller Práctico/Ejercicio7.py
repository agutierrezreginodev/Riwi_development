"""
Login con intentos y advertencias
Permite que un usuario introduzca una contraseña. Tiene 3 intentos.
• Si acierta, muestra “Acceso concedido” y detén el bucle.
• Si falla 2 veces, muestra un mensaje de advertencia.
• Si falla 3 veces, muestra “Acceso denegado, su cuenta ha sido bloqueada”.
"""

# Contraseña válida
valid_password = "adrian1611!"

for i in range(3):
    # Ingreso de datos por consola.
    user_password = input("Escriba su contraseña: ")
    # Se compara la contraseña ingresada por el usuario y la válida.
    if user_password == valid_password:
        # Si acierta la contraseña activa esta línea de código.
        print("Acceso concedido")
        break
    # Primer intento fallido
    elif i < 1:
        print("Contraseña incorrecta.")
    # Segundo intento fallido
    elif i < 2:
        print("Contraseña incorrecta, solo te queda 1 intento.")
    # Tercer intento fallido
    elif i < 3:
        print("Acceso denegado, su cuenta ha sido bloqueada")

