# ************************************************************************************************************** #

# Cifrado de Hill

# Info importante de las Matrices:
# Columnas = Reglones Verticales
# FIlas = Hileras Horizontales.
# ************************************************************************************************************** #
# Módulos:
import numpy as np
import random

# ************************************************************************************************************** #
# C I F R A D O

# Texto: marito es el mejor
# Clave de prueba: 35 53 12 12 21 5 2 4 1
# Texto cifrado: wyvqjfhlmedfubdlmr


# ************************************************************************************************************** #
# 1 - Función que transforma un texto a una matriz.


def texto_a_matriz():
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
        # Verificar si la matriz es invertible
        if np.linalg.det(matriz_clave) != 0:
            return matriz_clave
        else:
            print("La matriz no es invertible. Por favor, ingresa otros números.")


# Prueba de la función:
# print(clave_matriz())

# ************************************************************************************************************** #
# 3 - Función que multiplica ambas matrices y calcula el módulo 27:


def multiplica_y_modulo():
    matriz_text = texto_a_matriz()
    matriz_clav = clave_matriz()
    # Multiplicar las dos matrices
    resultado = np.dot(matriz_clav, matriz_text)
    # Calcular el módulo 27 de cada elemento de la matriz resultante
    resultado_modulo = np.mod(resultado, 27)
    return resultado_modulo


# Prueba de la función:
# print(multiplica_y_modulo())

# ************************************************************************************************************** #
# 4 - Función que transforma la matriz en una fila de numeros y les atribuye un caracter, para codificarlo:


def matriz_a_caract():
    # Crear una matriz de ejemplo
    matriz = multiplica_y_modulo()
    # Asegurarse de que la matriz tiene 3 filas
    assert matriz.shape[0] == 3, "La matriz debe tener 3 filas"
    # Aplanar la matriz a una sola fila
    matriz_aplanada = matriz.flatten(order='F')
    # Diccionario:
    mapeo = {i: chr(97 + i) for i in range(1, 27)}
    mapeo[27] = ' '  # Agregar el espacio como un carácter alfabético
    # Convertir los números en caracteres usando el diccionario del alfabeto
    caracter = ''.join(mapeo[num] for num in matriz_aplanada)
    print(mapeo)
    return caracter


# prueba Funcion
# print(matriz_a_caract())

# ************************************************************************************************************** #
# Programa principal:

cifrado = matriz_a_caract()
print(" ")
print("Tu texto cifrado es el siguiente: <  ", cifrado, " >")
print(" ")
print(" (No olvides tu clave secreta porque será la unica forma de descifrar el mensaje)")
print(" ")
# ************************************************************************************************************** #
# texto_a_matriz()
# clave_matriz()
# multiplica_y_modulo()
# matriz_a_caract()
# resultado_cifrado()
