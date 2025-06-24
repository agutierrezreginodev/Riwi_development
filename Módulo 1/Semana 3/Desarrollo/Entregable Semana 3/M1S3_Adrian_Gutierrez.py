import os
import time

# Lista de variables utilizadas en las funciones.
inventario = {}
nombre = ""
precio = 0
cantidad = 0

def añadirProducto(nombre, precio, cantidad):
    # Condicion para que se repita el bucle.
    seguirBucle = True
    while seguirBucle:
        try:
            # Se ingresan por consola el nombre, precio y cantidad del producto a ingresar al inventario.
            nombre = input("Escriba el nombre del producto: ").strip().capitalize()
            # Se valida que no se ingrese un espacio vacío en el nombre.
            if not nombre:
                raise ValueError
            precio = float(input("Digite el precio: "))
            cantidad = int(input("Digite la cantidad: "))
            # Se valida que el precio y la cantidad sean valores positivos.
            if precio <= 0 or cantidad <= 0:
                raise ValueError
            else:
                # Se crea en el inventario la clave que tendra como nombre el nuevo producto y su valor será otro diccionario,
                # con los pares clave-valor de precio y cantidad.
                inventario[nombre] = dict({"precio" : float(precio), "cantidad" : int(cantidad)})
                print(f"\n{nombre} ha sido añadido al inventario")
        except:
            # Excepción en caso tal se ingrese un dato no válido.
            print("\nEscribir un nombre de producto válido \nDebe ingresar números mayores que 0 \nNo se admiten letras ni caracteres especiales en precio y cantidad\n")
            time.sleep(1)
            os.system("cls")
            seguirBucle
        else:
            # Opción para preguntar de nuevo para añadir un producto.
            otroProducto = input("Desea ingresar otro producto? (s/n) ").lower()
            # Bucle para preguntar de nuevo en caso tal se ingrese un dato no válido.
            while otroProducto not in ['s', 'n']:
                print("Debe ingresar una opcion válida, 's' para añadir otro producto o 'n' para salir")
                otroProducto = input("Desea ingresar otro producto? (s/n)").lower()
            # Condicionales para cierre de bucle.
            if otroProducto == "s":
                seguirBucle
            elif otroProducto == "n":
                return inventario
            
def consultarProducto(nombre):
    # Condicion para que se repita el bucle.
    seguirBucle = True
    while seguirBucle:
        # Se ingresan por consola el nombre del producto a consultar del inventario.
        nombre = input("Escriba el nombre del producto que desea consultar: ").capitalize()
        if nombre in inventario:
            # Si el producto se encuentra en el inventario, muestra los datos del producto.
            resultado = (f"{nombre} se encuentra en el inventario \nLos datos obtenidos son {inventario[nombre]}")
            print(resultado)
        else:
            # Si el producto no se encuentra en el inventario, indica que no se encuentra en el inventario.
            resultado = (f"{nombre} no se encuentra en el inventario")
            print(resultado)
        # Opción para preguntar de nuevo para añadir un producto.
        otroProducto = input("Desea consultar otro producto? (s/n) ").lower()
        # Bucle para preguntar de nuevo en caso tal se ingrese un dato no válido.
        while otroProducto not in ['s', 'n']:
            print("Debe ingresar una opcion válida, 's' para consultar otro producto o 'n' para salir")
            otroProducto = input("Desea consultar otro producto? (s/n)").lower()
        # Condicionales para cierre de bucle.
        if otroProducto == "s":
            seguirBucle
        elif otroProducto == "n":
            seguirBucle = False

def actualizarPrecio(nombre, precio):
    # Condicion para que se repita el bucle.
    seguirBucle = True
    while seguirBucle:
        try:
            # Se ingresan por consola el nombre del producto a consultar del inventario.
            nombre = input("Escriba el nombre del producto que desea actualizar su precio: ").capitalize()
            if nombre in inventario:
                # Si el producto se encuentra en el inventario, permite ingresar el nuevo precio.
                precio = float(input("Digite el nuevo precio: "))
                if precio <= 0:
                    # Si se ingresa un precio menor a cero genera un error.
                    raise ValueError
                else:
                    # Si se ingresa un precio mayor a cero, se actualiza el valor.
                    inventario[nombre].update({"precio" : precio})
                    resultado = (f"El precio de {nombre} ha sido actualizado")
                    print(resultado)
            else:
                # Si el producto no se encuentra en el inventario, indica que no se encuentra en el inventario.
                resultado = (f"{nombre} no se encuentra en el inventario")
                print(resultado)
        except ValueError:
            # Excepción en caso tal se ingrese un dato no válido.
            print("\nDebe ingresar números mayores que 0 \nNo se admiten letras ni caracteres especiales en precio y cantidad\n")
            time.sleep(1)
            os.system("cls")
            seguirBucle
        else:
            # Opción para preguntar de nuevo para añadir un producto.
            otroProducto = input("Desea actualizar el precio de otro producto? (s/n) ").lower()
            # Bucle para preguntar de nuevo en caso tal se ingrese un dato no válido.
            while otroProducto not in ['s', 'n']:
                print("Debe ingresar una opcion válida, 's' para actualizar otro producto o 'n' para salir")
                otroProducto = input("Desea actualizar el precio de otro producto? (s/n)").lower()
            # Condicionales para cierre de bucle.
            if otroProducto == "s":
                seguirBucle
            elif otroProducto == "n":
                seguirBucle = False

def eliminarProducto(nombre):
    # Condicion para que se repita el bucle.
    seguirBucle = True
    while seguirBucle:
        # Se ingresan por consola el nombre del producto a consultar del inventario.
        nombre = input("Escriba el nombre del producto que desea eliminar: ").capitalize()
        if nombre in inventario:
            # Si el producto se encuentra en el inventario, permite eliminar dicho producto.
            inventario.pop(nombre)
            resultado = (f"{nombre} se ha eliminado del inventario")
            print(resultado)
        else:
            # Si el producto no se encuentra en el inventario, indica que no se encuentra en el inventario.
            resultado = (f"{nombre} no se encuentra en el inventario")
            print(resultado)
        # Opción para preguntar de nuevo para añadir un producto.
        otroProducto = input("Desea eliminar otro producto? (s/n) ").lower()
        # Bucle para preguntar de nuevo en caso tal se ingrese un dato no válido.
        while otroProducto not in ['s', 'n']:
            print("Debe ingresar una opcion válida, 's' para eliminar otro producto o 'n' para salir")
            otroProducto = input("Desea eliminar otro producto? (s/n)").lower()
        # Condicionales para cierre de bucle.
        if otroProducto == "s":
            seguirBucle
        elif otroProducto == "n":
            seguirBucle = False

def calcularValorTotal():
    # map() recorre el diccionario y los valores de cada clave, la función lambda realiza la operación de calcular el valor total 
    # de cada producto, y sum realiza la sumatoria de los valores totales de todos los productos dentro del diccionario.
    valor_total = sum(map(lambda nombre: nombre["precio"] * nombre["cantidad"], inventario.values()))
    print(f"El valor total del inventario es: {valor_total:.2f}")
        

def main():
    # Condicion para que se repita el bucle.
    seguirBucle = True
    while seguirBucle:
        try:
            # Se imprime en consola el menú de opciones.
            print("-"*43)
            print("          Sistema de inventario            ")
            print("-"*43)
            print("1. Añadir productos \n2. Consultar productos \n3. Actualizar precios \n4. Eliminar productos \n5. Calcular el valor total del inventario \n6. Mostrar inventario \n7. Salir \n")
            # Se selecciona una opción.
            opcionMenu = int(input("Elija una opción: "))
            match opcionMenu:
                case 1:
                    # Se llama a la función añadirProducto().
                    añadirProducto(nombre, precio, cantidad)
                    # Luego de 3 segundos se limpia la consola.
                    time.sleep(3)
                    os.system("cls")
                case 2:
                    # Se llama a la función consultarProducto().
                    consultarProducto(nombre)
                    # Luego de 3 segundos se limpia la consola.
                    time.sleep(3)
                    os.system("cls")
                case 3:
                    # Se llama a la función actualizarPrecio().
                    actualizarPrecio(nombre, precio)
                    # Luego de 3 segundos se limpia la consola.
                    time.sleep(3)
                    os.system("cls")
                case 4:
                    # Se llama a la función eliminarProducto().
                    eliminarProducto(nombre)
                    # Luego de 3 segundos se limpia la consola.
                    time.sleep(3)
                    os.system("cls")
                case 5:
                    # Se llama a la función calcularValorTotal().
                    calcularValorTotal()
                    # Luego de 3 segundos se limpia la consola.
                    time.sleep(3)
                    os.system("cls")
                case 6:
                    # Se imprime en consola el inventario.
                    print(inventario)
                    print("")
                    # Luego de 2 segundos se limpia la consola.
                    time.sleep(2)
                    os.system("cls")
                case 7:
                    # Se finaliza el programa.
                    print("\n¡Hasta luego!\n")
                    seguirBucle = False
        except:
            # Excepción en caso tal se ingrese un dato no válido.
            print("\nIngrese una opción válida\n")
            # Luego de 1 segundo se limpia la consola.
            time.sleep(1)
            os.system("cls")
            seguirBucle 
        

if __name__ == "__main__":
    main()
