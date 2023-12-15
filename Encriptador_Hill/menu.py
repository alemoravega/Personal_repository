# ************************************************************************************************************** #
# Definir una función para mostrar el menú


def mostrar_menu():
    print("""

███████╗███╗░░██╗░█████╗░██████╗░██╗██████╗░████████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝████╗░██║██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██╔██╗██║██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░███████║██║░░██║██║░░██║██████╔╝
██╔══╝░░██║╚████║██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░██╔══██║██║░░██║██║░░██║██╔══██╗
███████╗██║░╚███║╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░██║░░██║██████╔╝╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

██████╗░███████╗██████╗░░██████╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░  ██╗  
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░░░  ██║  
██████╔╝█████╗░░██████╔╝╚█████╗░██║░░██║██╔██╗██║███████║██║░░░░░  ██║  
██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║██║╚████║██╔══██║██║░░░░░  ╚═╝  
██║░░░░░███████╗██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░░██║███████╗  ██╗  
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝  ╚═╝  
""")
    print("Programado por DonPollo™ - 2023 All Rights Reserved. ")
    print(" ")
    print("----------------------")
    print("  Elige una opción:   ")
    print("----------------------")
    print(" ")
    print("1. Cifrar un mensaje")
    print(" ")
    print("2. Descifrar un mensaje")
    print(" ")
    print("3. Cerrar el programa")
    print(" ")


# Definir una variable para controlar el bucle
continuar = True
continuar1 = True
continuar2 = True

opcion = True
opcion1 = True
opcion2 = True
# Iniciar el bucle
while continuar:
    # Mostrar el menú
    mostrar_menu()
    # Pedir al usuario que elija una opción
    opcion = input("Introduce el número de la opción: ")
    print(" ")
    # Ejecutar la opción elegida
    if opcion == "1":
        while continuar1:
            print(" ")
            print("Tu texto cifrado es: < ", cif_final(), " >")
            print(" ")
            clave = clave_cif()
            print("Tu clave es: <", clave.flatten(), ">")
            print(" ")
            print("¡Recuerda guardarla!")
            print("")
            # Pedir al usuario que elija una opción
            opcion1 = input("¿Deseas volver al menú principal? s/n: ")
            # Ejecutar la opción elegida
            if opcion1 == "s" or opcion1 == "S":
                continuar1 = False
            elif opcion1 == "n" or opcion1 == "N":
                continuar1 = True
            else:
                # Imprimir un mensaje de error
                print(" ")
                print("Opción inválida. Vuelve a intentarlo.")
            print(" ")
    elif opcion == "2":
        while continuar2:
            print(" ")
            print("Tu texto DESCIFRADO es: < ", desc_final(), " >")
            print(" ")
            # Pedir al usuario que elija una opción
            opcion2 = input("¿Deseas volver al menú principal? s/n: ")
            # Ejecutar la opción elegida
            if opcion2 == "s" or opcion2 == "S":
                continuar2 = False
            elif opcion2 == "n" or opcion2 == "N":
                continuar2 = True
            else:
                # Imprimir un mensaje de error
                print(" ")
                print("Opción inválida. Vuelve a intentarlo.")
                print(" ")
    elif opcion == "3":
        # Salir del bucle
        continuar = False
        # Imprimir un mensaje de despedida
        print(" ")
        print("Gracias por usar el programa. ¡Hasta pronto!")
        print(" ")
    else:
        # Imprimir un mensaje de error
        print(" ")
        print("Opción inválida. Por favor, elige una de las opciones del menú.")
        print(" ")

# Texto: marito es el mejor
# Clave de prueba: 35 53 12 12 21 5 2 4 1
# Texto cifrado: wyvqjfhlmedfubdlmr

# don pollo es el mejor - 35 53 12 12 21 5 2 4 1 - xbbcgzvmghlmedfubdlmr
