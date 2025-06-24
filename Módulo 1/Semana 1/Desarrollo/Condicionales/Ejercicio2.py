"""
Una persona ingresa su edad. Clasifica esa edad en una de las siguientes categorías:
Menor de edad (<18).
Adulto joven (18 a 30).
Adulto maduro (31 a 65).
Adulto mayor (>65).
"""

edad = int(input("Digite su edad: "))

if edad > 65:
    print("Adulto mayor.")
elif edad >= 31 and edad <= 65:
    print("Adulto maduro")
elif edad >= 18 and edad <= 30:
    print("Adulto joven")
elif edad <= 18:
    print("Menor de edad")