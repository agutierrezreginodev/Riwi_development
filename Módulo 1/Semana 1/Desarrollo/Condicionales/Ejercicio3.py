"""
Tarifa de transporte según día y hora
Un usuario indica si el día es laborable (“S”/“N”) y la hora del día (0 a 23). Calcula la tarifa aplicable:
Día laborable:
PICO si la hora está entre 7 a 9 o 17 a 19 (inclusive).
NORMAL en cualquier otra hora. 
Fin de semana (día no laborable): 
FIN DE SEMANA.
"""

tarifa_base = 3000
tarifa_total = 0

dia_laboral = input("Es un día laboral? (S/N): ").lower()

if dia_laboral == "s":
    hora = int(input("Ingrese la hora: "))
    if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
        tarifa_total = tarifa_base + 500
    else:
        tarifa_total = tarifa_base + 200
elif dia_laboral == "n":
    tarifa_total = tarifa_base + 500
else:
    print("Opción inválida")


print(f"La tarifa a pagar es: {tarifa_total}")