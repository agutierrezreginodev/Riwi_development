# Calcular el costo total de una compra en una tienda.
while True:
    # Utilizamos try para que en caso ingresen caracteres donde deben ir números nos muestre un mensaje.
    try:
        # Solicitar datos por consola.
        product_name = input("Escriba el nombre del producto: ")
        unit_price = float(input("Digite el precio por unidad: "))
        product_qty = int(input("Digite la cantidad de productos: "))
        product_dct = int(input("Digite porcentaje de descuento: "))
    except:
        print("Debe ingresar valores numéricos en las casillas diferentes al nombre del producto")
        exit()

    while True:
        # Condicional para asegurar que los valores numéricos sean positivos.
        if unit_price < 0 or product_qty < 0 or product_dct < 0:
            print("Verifique los datos ingresados, deben ser unidades positivas.")
            break
        else:
            # Cálculo de costo sin aplicar descuento.
            price_wo_dct = unit_price * product_qty
            # Cálculo del monto descontado.
            dct = price_wo_dct * (product_dct / 100)
            # Cálculo del precio total
            full_price = price_wo_dct - dct
            # Imprimir costo total (descuento incluído)
            print(f"Costo sin descuento: {price_wo_dct} \nDescuento: {dct} \nPrecio total de {product_name}: {full_price:.2f}")
            break

    # Realizar compras adicionales
    while True:
        another_purch = input("Desea realizar otra compra? (s/n): ").lower()
        if another_purch == "s":
            break
        elif another_purch == "n":
            exit()
        else:
            print("Ingrese una opción válida")
            continue