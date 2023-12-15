# ************************************************************************************************************** #

# Cifrado de Hill

# Info importante de las Matrices:
# Columnas = Reglones Verticales
# FIlas = Hileras Horizontales.
# ************************************************************************************************************** #
# Módulos:
import string
import numpy as np
import random

# ************************************************************************************************************** #
# D E S C I F R A D O - P R U E B A S

# Texto ingresado: marito es el mejor
# Clave : 35 53 12 12 21 5 2 4 1
# texto cifrado: axqpgqehgubrzbe

# ************************************************************************************************************** #

# 1 - Función que transforma un texto CIFRADO a una matriz.


def cifrado_a_matriz():
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


def clave_matriz():
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

def multiplica_ambas():
    matriz_text = cifrado_a_matriz()
    matriz_clav = clave_matriz()
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

# Programa principal:

# ************************************************************************************************************** #


descifrado = multiplica_ambas()
print(" ")
print("Tu texto descifrado es el siguiente: <  ", descifrado, " >")
print(" ")
