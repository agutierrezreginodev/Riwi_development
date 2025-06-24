# Calcular el costo total de una compra en una tienda.
product_name = input("Escriba el nombre del producto: ")
unit_price = float(input("Digite el precio por unidad: "))
product_qty = int(input("Digite la cantidad de productos: "))
product_dct = int(input("Digite porcentaje de descuento: "))

# Cálculo de costo sin aplicar descuento.
price_wo_dct = unit_price * product_qty
# Cálculo del monto descontado.
dct = price_wo_dct * (product_dct / 100)
# Cálculo del precio total
full_price = price_wo_dct - dct
# Imprimir costo total (descuento incluído)
print(f"Costo sin descuento: {price_wo_dct} \nDescuento: {dct} \nPrecio total de {product_name}: {full_price:.2f}")