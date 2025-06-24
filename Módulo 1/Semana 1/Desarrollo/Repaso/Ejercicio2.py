"""
Lee y muestra nombre y edad
Pide al usuario su nombre y edad, luego muestra un mensaje como:
 "Hola [nombre], tienes [edad] años."
"""

name = input("Escribe tu nombre: ")
age = int(input("Ingresa tu edad: "))

print(f"Hola {name}, tienes {age} años.")