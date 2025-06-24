"""
Se realiza el entrenamiento de la semana 2, implementando funciones:

1.  Determinar el estado de aprobación
2.  Calcular el promedio
3.  Contar calificaciones mayores
4.  Verificar y contar calificaciones específicas
"""

nota = 0
nota_minima = 70
listaNotas = []
notasMayores = []

def estadoNota(nota):
    while True:
        try:
            nota = int(input("Ingrese una calificación: "))
            
            if nota >= nota_minima and nota <= 100:
                mensajeEstado = print(f"Aprobado. La nota mínima para pasar es {nota_minima}")
                return mensajeEstado
            elif nota < nota_minima and nota >= 0:
                mensajeEstado = print(f"Reprobado. La nota mínima para pasar es {nota_minima}")
                return mensajeEstado
            else:
                print("Digite una nota válida")
                continue
            
        except ValueError:
            print("Debe ingresar un valor numérico.")
            continue

def splitNotas(nota):
    while True:
        try:
            nota = input("Digite las notas (entre 0 y 100) una por una seguida de coma: \n")
            
            notasSplit = nota.split(",")
            
            for i in notasSplit:
                if int(i) < 0 or int(i) > 100:
                    raise ValueError
                else:
                    listaNotas.append(int(i))

            printlista = print(f"Tus notas son {listaNotas}.")
            return printlista       
        
        except ValueError:
            print("Digite la nota de nuevo.")
            print("No se deben ingresar letras y solo se aceptan números entre 0 y 100. \n")
            continue

def promedioNotas(listaNotas):
    sumNotas = 0
    cantNotas = 0

    for i in listaNotas:
        sumNotas += i
        cantNotas += 1

    prom = sumNotas/cantNotas

    mensajePromedio = print(f"Tu promedio es ---> {prom}")
    return mensajePromedio

def notaMayorRef(listaNotas):
    cantNotas = 0

    notaRef = int(input("Digite nota de referencia (entre 0 y 100): "))
    
    for i in listaNotas:
        if i > notaRef:
            notasMayores.append(i)
            cantNotas += 1
    
    mensajeMayores = print(f"Tus notas son {listaNotas} \nLas notas mayores a {notaRef} son {cantNotas} que son ---> {notasMayores}")
    return mensajeMayores

def verificarNotaEspecifica(listaNotas):
    cantNotas = 0

    verificarNota = int(input("Digite nota que desea verificar (entre 0 y 100): "))
    
    for i in listaNotas:
        if i == verificarNota:
            cantNotas += 1
        
    if cantNotas > 0:
        mensajeVerificacion = print(f"La nota {verificarNota} si se encuentra en la lista. \nLa cantidad de notas iguales a {verificarNota} son ---> {cantNotas}")
        return mensajeVerificacion
    else:
        mensajeVerificacion = print(f"La nota {verificarNota} no se encuentra en la lista.")
        return mensajeVerificacion

def main():
    while True:
        try: 
            print("Menú Principal")
            print("1. Determinar el estado de aprobación de una nota. \n2. Calcular el promedio. \n3. Contar calificaciones mayores. \n4. Verificar y contar calificaciones específicas. \n")
            opcionMenu = int(input("Digite una opción: "))

            match opcionMenu:
                case 1:
                    estadoNota(nota)
                    break
                case 2:
                    splitNotas(nota)
                    promedioNotas(listaNotas)
                    break
                case 3:
                    splitNotas(nota)
                    notaMayorRef(listaNotas)
                    break
                case 4:
                    splitNotas(nota)
                    verificarNotaEspecifica(listaNotas)
                    break
                case _:
                    print("Digite una opción correcta.")
                    continue
        except ValueError:
            print("No se puede ingresar letras. \nSolo se aceptan notas de 0 a 100.")

if __name__ == "__main__":
    main()