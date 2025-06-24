"""
Convertidor de Edad
● Pide al usuario que ingrese su edad en años y muestra su edad en meses
(suponiendo 12 meses por año).
"""

edad = int(input("Digite su edad: "))

edad_meses = edad * 12

print(f"Su edad en meses es: {edad_meses} meses")