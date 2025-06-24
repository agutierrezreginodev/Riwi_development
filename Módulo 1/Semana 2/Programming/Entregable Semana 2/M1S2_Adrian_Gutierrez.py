"""
El programa que vas a desarrollar en este entrenamiento debe:

1.  Determinar el estado de aprobación:
    * Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    * Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
2.  Calcular el promedio:
    * Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    * Calcular y mostrar el promedio de las calificaciones en la lista
3.  Contar calificaciones mayores:
    * Preguntar al usuario por un valor específico
    * Contar cuántas calificaciones en la lista son mayores que este valor
4.  Verificar y contar calificaciones específicas
    * Preguntar al usuario por una calificación específica. 
    * Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y 
    continue para controlar el flujo del programa.
"""

# Menú opciones
try:
    print("Menú Principal")
    print("1. Determinar el estado de aprobación de una nota.")
    print("2. Calcular el promedio de notas.")
    print("3. Contar calificaciones mayores.")
    print("4. Verificar y contar calificaciones específicas.\n")

    opcion_menu = int(input("Seleccione una opción: "))

    # Nota mínima para aprobar.
    nota_minima = 70
    # Lista de notas de tipo entero para hacer comparaciones.
    lista_notas = []
    # Lista de notas mayor a nota de referencia.
    notas_mayores_ref = []
    # Sumatoria de notas.
    sum_notas = 0
    # Cantidad de notas.
    cant_notas = 0

    match opcion_menu:
        # Opción 1
        case 1:
            while True:
                try:
                    # Si ingresa una nota y se valida si aprobó o no.
                    nota = int(input("Ingrese una calificación: "))
                    # Nota aprobada
                    if nota >= nota_minima and nota <= 100:
                        print(f"Aprobado. La nota para pasar es {nota_minima}")
                        break
                    # Nota reprobada
                    elif nota < nota_minima and nota >= 0:
                        print(f"Reprobado. La nota para pasar es {nota_minima}")
                        break
                    # Nota no válida
                    else:
                        print("Digite una nota válida")
                        continue
                except ValueError:
                    print("Debe ingresar un valor numérico. \n")
                    continue
        # Opción 2
        case 2:
            while True:
                try:
                    # Calcular el promedio de n cantidad de notas, requeridas por el usuario.
                    nota = input("Digite las notas (entre 0 y 100) a promediar una por una seguida de coma: \n")
                    # Dividir una por una cada nota que se ingresó en el string.
                    notas_obo = nota.split(",")
                    # Añadimos a lista de notas, cada nota spliteada en formato int para poder operar con los valores.
                    for i in notas_obo:
                        # Si hay una nota fuera del rango se genera un error, para que el usuario la ingrese de nuevo.
                        if int(i) < 0 or int(i) > 100:
                            raise ValueError
                        else:
                            lista_notas.append(int(i))
                    # Realizamos la sumatoria de las notas ingresadas y realizamos el conteo de la cantidad de notas.
                    for i in lista_notas:
                        sum_notas += i
                        cant_notas += 1
                    # Cálculo del promedio de notas
                    prom = sum_notas/cant_notas
                    # Imprimimos en pantalla el promedio y las notas.
                    print(f"Tus notas son {lista_notas} \nTu promedio es ---> {prom}")
                    break
                except ValueError:
                    print("Digite la nota de nuevo.")
                    print("No se deben ingresar letras y solo se aceptan números entre 0 y 100. \n")
                    continue
        # Opción 3
        case 3:
            while True:
                try:
                    # Contar calificaciones mayores a una nota de referencia.
                    nota = input("Digite las notas (entre 0 y 100) a promediar una por una seguida de coma: \n")
                    # Dividir una por una cada nota que se ingresó en el string.
                    notas_obo = nota.split(",")
                    # Añadimos a lista de notas, cada nota spliteada en formato int para poder operar con los valores.
                    for i in notas_obo:
                        # Si hay una nota fuera del rango se genera un error, para que el usuario la ingrese de nuevo.
                        if int(i) < 0 or int(i) > 100:
                            raise ValueError
                        else:
                            lista_notas.append(int(i))
                    # Se ingresa por consola nota de referencia.
                    nota_ref = int(input("Digite nota de referencia (entre 0 y 100): "))
                    # Se añaden a la lista las notas mayores a la nota de referencia y se cuentan dichas notas.
                    for i in lista_notas:
                        if i > nota_ref:
                            notas_mayores_ref.append(i)
                            cant_notas += 1
                    # Imprimimos en pantalla las notas y cantidad.
                    print(f"Tus notas son {lista_notas} \nLas notas mayores a {nota_ref} son {cant_notas} que son ---> {notas_mayores_ref}")
                    break
                except ValueError:
                    print("Digite la nota de nuevo.")
                    print("No se deben ingresar letras y solo se aceptan números entre 0 y 100. \n")
                    continue
        # Opción 4
        case 4:
            while True:
                try:
                    # Contar calificaciones iguales a la que se desea verificar.
                    nota = input("Digite las notas (entre 0 y 100) a promediar una por una seguida de coma: \n")
                    # Dividir una por una cada nota que se ingresó en el string.
                    notas_obo = nota.split(",")
                    # Añadimos a lista de notas, cada nota spliteada en formato int para poder operar con los valores.
                    for i in notas_obo:
                        # Si hay una nota fuera del rango se genera un error, para que el usuario la ingrese de nuevo.
                        if int(i) < 0 or int(i) > 100:
                            raise ValueError
                        else:
                            lista_notas.append(int(i))
                    # Se ingresa por consola nota de referencia.
                    verificar_nota = int(input("Digite nota que desea verificar (entre 0 y 100): "))
                    # Realizamos el conteo de la cantidad de notas iguales a la de referencia.
                    for i in lista_notas:
                        if i == verificar_nota:
                            cant_notas += 1
                    # Se imprime un texto de acuerdo a si la nota de referencia se encuentra en nuestra lista de notas.
                    if cant_notas > 0:
                        print(f"La nota {verificar_nota} si se encuentra en la lista. \nLa cantidad de notas iguales a {verificar_nota} son ---> {cant_notas}")
                        break
                    else:
                        print(f"La nota {verificar_nota} no se encuentra en la lista.")
                        break
                except ValueError:
                    print("Digite la nota de nuevo.")
                    print("No se deben ingresar letras y solo se aceptan números entre 0 y 100. \n")
                    continue
        # Ninguna de las opciones mencionadas
        case __:
            print("Digite una opción válida.")
except ValueError:
    print("Ingrese una opción válida. \n")
