"""
Suma de dos números
Pide al usuario dos números y muestra la suma de ambos.

Resta de dos números
Pide al usuario dos números y muestra la resta del primero menos el segundo.

Multiplicación de dos números
Pide al usuario dos números y muestra el resultado de multiplicarlos.

División de dos números
Pide al usuario dos números y muestra el resultado de dividir el primero por el segundo.
Asegúrate de que el segundo número no sea cero.
"""

while True:
    print("Menú de operaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    option = int(input("Elija una opción: "))

    match option:
        case 1:
            num1 = int(input("Digite número 1: "))
            num2 = int(input("Digite número 2: "))
            sum = num1 + num2
            print(f"La suma es {sum}")
            break
        case 2:
            num1 = int(input("Digite número 1: "))
            num2 = int(input("Digite número 2: "))
            res = num1 - num2
            print(f"La resta es {res}")
            break
        case 3:
            num1 = int(input("Digite número 1: "))
            num2 = int(input("Digite número 2: "))
            mult = num1 * num2
            print(f"La multiplicación es {mult}")
            break
        case 4:
            num1 = int(input("Digite número 1: "))
            num2 = int(input("Digite número 2: "))
            try:
                div = num1 / num2
                print(f"La división es {div:.4}")
                break
            except:
                print("No se puede dividir entre cero")
        case __:
            print("Digite una opción válida.")
            continue