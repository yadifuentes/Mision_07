#Yadira Fuentes Calderón, A01745235
#Programa que realiza tres acciones (dividir, encontrar numero mayor y salir)

def dividir(dividiendo,divisor):
    numeroDividiendo= dividiendo
    cociente= 0

    while dividiendo>=divisor:
        dividiendo= dividiendo-divisor
        cociente+=1

    print(numeroDividiendo,"/",divisor,"=",cociente,", sobra",dividiendo)
    print()


def encontrarMayor():
    numero = 0
    numeroMayor = 0

    print("Teclea una serie de números para encontrar el mayor.")
    numero= int(input("Teclea el número [-1 para salir]: "))


    if numero != -1:
        while numero != -1:
            if numero >= 0:
                if numero >= numeroMayor:
                    numeroMayor= numero
            numero = int(input("Teclea el número [-1 para salir]: "))
        print("El mayor es:", numeroMayor)
        print()
    else:
        print ("No hay valor mayor")
        print()

def main():
    print("Misión 07. Ciclos while")
    print("Autor: Yadira Fuentes Calderón")
    print("Matrícula: A01745235")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    print()

    while opcion !=3:
        if opcion==1:
            dividiendo= int(input("Dividiendo: "))
            divisor= int(input("Divisor: "))
            dividir(dividiendo,divisor)

        elif opcion==2:
            encontrarMayor()

        elif opcion<0 or opcion>3:
            print("ERROR, teclea 1, 2 o 3")
            print()
        opcion = int(input("""Misión 07. Ciclos while
Autor: Yadira Fuentes Calderón
Matrícula: A01745235
1. Calcular divisiones
2. Encontrar el mayor
3. Salir"
Teclea tu opción: """))
        print()

    print("Gracias por usar este programa, regresa pronto")


main()
