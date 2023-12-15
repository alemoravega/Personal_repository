# ************************************************************************************************************** #
# Encriptador con Cifrado de Hill

# Info importante de las Matrices:
# Columnas = Reglones Verticales
# FIlas = Hileras Horizontales.

# ************************************************************************************************************** #

# Módulos:

import numpy as np
import random

# ************************************************************************************************************** #
# F U N C I O N E S   D E   C I F R A D O
# ************************************************************************************************************** #
# 1 - Función que transforma un texto a una matriz.


def text_cif():
    # Solicitar el texto al usuario
    print(" ")
    texto = input("Ingresa el texto a codificar: ")
    print(" ")
    # Transformar el texto a minúsculas
    texto = texto.lower()
    # Mapear cada carácter a un número
    mapeo = {chr(96 + i): i for i in range(1, 27)}
    mapeo[' '] = 27  # Agregar el espacio como el último carácter
    # Transformar el texto a números
    texto_numerico = [mapeo[caracter]
                      for caracter in texto if caracter in mapeo]
    # Calcular el número de columnas
    n_filas = 3
    n_columnas = int(np.ceil(len(texto_numerico) / n_filas))
    # Agregar espacios si es necesario
    while len(texto_numerico) < n_filas * n_columnas:
        texto_numerico.append(mapeo[' '])  # Agregar el espacio
    # Crear una matriz con un número variable de columnas y 3 filas
    matriz_txt = np.array(texto_numerico).reshape(n_columnas, n_filas).T
    return matriz_txt


# Prueba de la función:
# print(texto_a_matriz())

# ************************************************************************************************************** #
# 2 - Función que pide ingresar una clave de nueve digitos y lo transforma a una matriz de 3 x 3:


def clave_cif():
    while True:
        # Solicitar los números al usuario
        clave = input(
            "Por favor, ingresa tu clave de 9 números separados por espacios: ")
        # Transformar los números a una lista de enteros
        clave = list(map(int, clave.split()))
        # Asegurarse de que se ingresaron exactamente 9 números
        if len(clave) != 9:
            print("Debes ingresar exactamente 9 números.")
            continue
        # Crear una matriz con 3 filas y 3 columnas
        matriz_clave = np.array(clave).reshape(3, 3)
        # Verificar si la matriz es invertible
        if np.linalg.det(matriz_clave) != 0:
            return matriz_clave
        else:
            print("La matriz no es invertible. Por favor, ingresa otros números.")


# Prueba de la función:
# print(clave_matriz())

# ************************************************************************************************************** #
# 3 - Función que multiplica ambas matrices y calcula el módulo 27:


def mod_cif():
    matriz_text = text_cif()
    matriz_clav = clave_cif()
    # Multiplicar las dos matrices
    resultado = np.dot(matriz_clav, matriz_text)
    # Calcular el módulo 27 de cada elemento de la matriz resultante
    resultado_modulo = np.mod(resultado, 27)
    return resultado_modulo


# Prueba de la función:
# print(multiplica_y_modulo())

# ************************************************************************************************************** #
# 4 - Función que transforma la matriz en una fila de numeros y les atribuye un caracter, para codificarlo:


def cif_final():
    # Crear una matriz de ejemplo
    matriz = mod_cif()
    # Asegurarse de que la matriz tiene 3 filas
    assert matriz.shape[0] == 3, "La matriz debe tener 3 filas"
    # Aplanar la matriz a una sola fila
    matriz_aplanada = matriz.flatten(order='F')
    # Redondear los valores de la matriz aplanada a enteros
    matriz_aplanada = matriz_aplanada.round().astype(int)
    # Diccionario:
    mapeo = {i: chr(97 + i) for i in range(1, 27)}
    mapeo[27] = ' '  # Agregar el espacio como un carácter alfabético
    # Convertir los números en caracteres usando el diccionario del alfabeto
    caracter = ''.join(mapeo[num] for num in matriz_aplanada)
    return caracter


# prueba Funcion
# print(matriz_a_caract())


# ************************************************************************************************************** #
# F U N C I O N E S   D E   D E S C I F R A D O
# ************************************************************************************************************** #

# 1 - Función que transforma un texto CIFRADO a una matriz.


def text_desc():
    # Solicitar el texto al usuario
    cifrado = input("Ingresa el texto a decodificar: ")
    # Transformar el texto a minúsculas
    cifrado = cifrado.lower()
    # Mapear cada carácter a un número
    mapeo = {chr(97 + i): i for i in range(1, 27)}
    mapeo[' '] = 27  # Agregar el espacio como un carácter alfabético
    # Transformar el cifrado a números
    cifrado_numerico = [mapeo[caracter]
                        for caracter in cifrado if caracter in mapeo]
    # Calcular el número de columnas
    n_filas = 3
    n_columnas = int(np.ceil(len(cifrado_numerico) / n_filas))
    # Agregar espacios si es necesario
    while len(cifrado_numerico) < n_filas * n_columnas:
        cifrado_numerico.append(mapeo[' '])  # Agregar el espacio
    # Crear una matriz con un número variable de columnas y 3 filas
    matriz_cif = np.array(cifrado_numerico).reshape(n_columnas, n_filas).T
    return matriz_cif

# Prueba función:
# print(cifrado_a_matriz())

# ************************************************************************************************************** #
# 2 - Función que pide ingresar una clave de nueve digitos y lo transforma a una matriz de 3 x 3; calcula su inverso
# y lo divide por mod 27:


def clave_desc():
    while True:
        # Solicitar los números al usuario
        clave = input(
            "Por favor, ingresa tu clave de 9 números separados por espacios: ")
        # Transformar los números a una lista de enteros
        clave = list(map(int, clave.split()))
        # Asegurarse de que se ingresaron exactamente 9 números
        if len(clave) != 9:
            print("Debes ingresar exactamente 9 números.")
            continue
        # Crear una matriz con 3 filas y 3 columnas
        matriz_clave = np.array(clave).reshape(3, 3)
        # Verificar si la matriz es invertible e invertirla:
        if np.linalg.det(matriz_clave) != 0:
            A_inv = np.linalg.inv(matriz_clave)
            # Calcula el Mod 27 de la matriz:
            M_mod = np.mod(A_inv, 27)
            return M_mod
        else:
            print("La matriz no es invertible. Por favor, ingresa otros números.")


# Prueba de la función:
# clave_matriz()

# ************************************************************************************************************** #
# 3 - Función que multiplica ambas matrices, divide por mod 27 y el resultado lo transforma a letras:

def desc_final():
    matriz_text = text_desc()
    matriz_clav = clave_desc()
    # Multiplicar las dos matrices
    resultado = np.dot(matriz_clav, matriz_text)
    matriz_fin = np.mod(resultado, 27)
    matriz_apla = matriz_fin.flatten(order='F')
    # Usamos la función round para convertir los elementos a enteros
    matriz_apla = [round(x) for x in matriz_apla]
    # Retornamos la cadena de letras
    return "".join([chr(i + 96) if i != 27 else " " for i in matriz_apla])


# Prueba Función:
# multiplica_ambas()

# ************************************************************************************************************** #
# P R O G R A M A   P R I N C I P A L

# ************************************************************************************************************** #
# Definir una función para mostrar el menú


def mostrar_menu():

    print(" ")
    # Imprimir las opciones
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
    print("----------------------")
    print("  Elige una opción:    ")
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
            # Pedir al usuario que elija una opción
            opcion1 = input("¿Deseas volver al menú principal? s/n: ")
            # Ejecutar la opción elegida
            if opcion1 == "s" or opcion1 == "S":
                continuar1 = True
            elif opcion1 == "n" or opcion1 == "N":
                continuar1 = False
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
                continuar2 = True
            elif opcion2 == "n" or opcion2 == "N":
                continuar2 = False
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
