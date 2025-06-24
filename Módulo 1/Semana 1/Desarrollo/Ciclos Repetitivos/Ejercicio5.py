"""
Verificador de edad
Crea un menú interactivo (while True) donde se pregunte continuamente la edad 
del usuario hasta que una edad mayor o igual a 18 sea ingresada. Usa break adecuadamente.
"""

while True:
    edad = int(input("Ingrese su edad: "))
    if edad < 18 and edad > 0:
        print("Ingrese de nuevo su edad.")
        continue
    elif edad < 0:
        print("Debe ingresar un valor mayor a cero")
        continue
    else:
        break