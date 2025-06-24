"""
Verificar si una persona es mayor de edad
Pide al usuario su edad y muestra si es mayor o menor de edad (mayor o igual a 18 años).
"""

age = int(input("Ingrese su edad: "))

if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")