"""
Validación de contraseña simple
El usuario crea una contraseña que debe cumplir dos requisitos:
Tener al menos 8 caracteres.
Contener al menos el carácter @.
Si la longitud es insuficiente, informar “Contraseña muy corta”. Si la longitud es correcta pero falta @, informar “La contraseña debe incluir al menos un '@'”.
Sólo cuando ambos requisitos se cumplan, mostrar “Contraseña válida”.
"""

contraseña = input("Ingrese una contraseña: ")

if (len(contraseña) >= 8) and ('@' in contraseña):
    print("Contraseña válida")
elif (len(contraseña) >= 8) and ('@' not in contraseña):
    print("La contraseña debe incluir al menos un '@'")
elif (len(contraseña) < 8):
    print("Contraseña muy corta")