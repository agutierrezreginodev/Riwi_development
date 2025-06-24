"""
Calculadora de IMC
● Diseña un algoritmo que calcule el Índice de Masa Corporal (IMC) de una
persona. Solicita al usuario que ingrese su peso en kg y su altura en metros.
"""

import math

peso = float(input("Digite su peso (kg): "))
altura = float(input("Digite su altura (m): "))

imc = peso/math.pow(altura, 2)

print(f"Su indice de masa corporal es {imc:.4}")