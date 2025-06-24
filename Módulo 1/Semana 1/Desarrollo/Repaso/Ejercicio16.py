"""
Validar una contraseña
Define una contraseña predefinida.
Pide al usuario que ingrese una contraseña hasta que la escriba correctamente.
"""

valid_pass = "Adrian12345"

while True:
    user_pass = input("Ingrese su contraseña: ")
    if user_pass == valid_pass:
        print("Acceso permitido")
        break
    else:
        print("Acceso denegado")
        continue