"""
Descuento en tienda según monto y tipo de cliente
Enunciado:
Un cliente ingresa el monto de su compra y si es VIP (“S”/“N”). Aplica el siguiente descuento:
VIP:
20 % si monto ≥ 500.
10 % si monto < 500.
No VIP:
5 % si monto ≥ 500.
0 % si monto < 500.
"""

monto = float(input("Digite monto de compra: "))
membresia = input("Es miembro VIP? (S/N): ").lower()
total = 0

if membresia == "s":
    if monto >= 500:
        total = monto * 0.8
    elif monto < 500:
        total = monto * 0.9
elif membresia == "n":
    if monto >= 500:
        total = monto * 0.95
    elif monto < 500:
        total = monto
else:
    print("Opción inválida")

print(f"Monto total a pagar: {total}")