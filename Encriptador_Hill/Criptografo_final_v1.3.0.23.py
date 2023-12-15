# ************************************************************************************************************** #
# Encriptador con Cifrado de Hill

# Info importante de las Matrices:
# Columnas = Reglones Verticales
# FIlas = Hileras Horizontales.

# ************************************************************************************************************** #

# Módulos:

import numpy as np
import random
from numpy.linalg import LinAlgError
from sympy import Matrix

# ************************************************************************************************************** #
# F U N C I O N E S   D E   C I F R A D O
# ************************************************************************************************************** #
# 1 - Función que transforma un texto a una matriz.


def text_cif():
    # Solicitar el texto al usuario
    texto = ("don pollo es el mejor")
    # Transformar el texto a minúsculas
    texto = texto.lower()
    # Mapear cada carácter a un número
    mapeo = {chr(97 + i): i for i in range(26)}
    mapeo[' '] = 26  # Agregar el espacio como un carácter alfabético
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


# Prueba de la función:             REVISADOOOOOOOOOOO
# print(text_cif())

# ************************************************************************************************************** #
# 2 - Función que genera una clave de nueve digitos de forma aleatoria y lo transforma a una matriz de 3 x 3:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(x, y):
    return gcd(x, y) == 1


def clave_cif():
    while True:
        matrix = np.random.randint(1, 26, size=(3, 3))
        determinant = round(np.linalg.det(matrix))
        try:
            inv_matrix = np.linalg.inv(matrix)
            if determinant != 0 and is_coprime(determinant, 27):
                return matrix
        except LinAlgError:
            pass


# Prueba de la función:   REVISADOOOOOOOO
print("tu clave es: ", clave_cif().flatten())

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
    mapeo = {i: chr(97 + i) for i in range(26)}
    mapeo[26] = ' '  # Agregar el espacio como un carácter alfabético
    # Convertir los números en caracteres usando el diccionario del alfabeto
    caracter = ''.join(mapeo[num] for num in matriz_aplanada)
    print("texto cifrado: ", caracter)
    return caracter


# prueba Funcion
# print(cif_final())


# ************************************************************************************************************** #
# F U N C I O N E S   D E   D E S C I F R A D O
# ************************************************************************************************************** #

# 1 - Función que transforma un TEXTO CIFRADO a una matriz.


def text_desc():
    # Solicitar el texto al usuario
    cifrado = input("Ingresa el texto cifrado: ")
    # Transformar el texto a minúsculas
    cifrado = cifrado.lower()
    # Mapear cada carácter a un número
    mapeo = {chr(97 + i): i for i in range(26)}
    mapeo[' '] = 26  # Agregar el espacio como un carácter alfabético
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


# Prueba función: RAVISAAAADOOOOO
# print(text_desc())

# ************************************************************************************************************** #
# 2 - Función que pide ingresar una clave de nueve digitos y lo transforma a una matriz de 3 x 3;


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
            return matriz_clave
        else:
            print("La matriz no es invertible. Por favor, ingresa otros números.")


# Prueba de la función:  REVISADOOOOO
# print(clave_desc())

# ************************************************************************************************************** #
# 3 - Función que calcula la matriz inversa y luego el modulo 27:


def desc_inv_mod():
    A = clave_desc()
    # Verifica si la matriz es cuadrada
    if A.shape[0] != A.shape[1]:
        return "Error: La matriz debe ser cuadrada"
    # Verifica si la matriz es invertible
    if np.linalg.det(A) == 0:
        return "Error: La matriz no es invertible"
    # Calcula la inversa de la matriz
    A_inv = np.linalg.inv(A)
    # Divide la matriz inversa por mod 27
    A_inv_mod = np.mod(A_inv, 27)
    return A_inv_mod


# Prueba de la función:     REVISADOOOOOOOOOOOOO
# print(calcular_inversa())


# ************************************************************************************************************** #
# 4 - Función que multiplica ambas matrices, divide por mod 27 y el resultado lo transforma a letras:


def desc_final():
    matriz_text = text_desc()
    matriz_clav = desc_inv_mod()
    # Multiplicar las dos matrices
    resultado = np.dot(matriz_clav, matriz_text)
    # Redondear al entero más cercano y luego aplicar mod 27
    resultado_round = np.round(resultado)
    matriz_fin = np.mod(resultado_round, 27)
    matriz_apla = matriz_fin.flatten(order='F')
    # Usamos la función round para convertir los elementos a enteros
    matriz_apla1 = [round(x) for x in matriz_apla]
    # Diccionario:
    mapeo = {i: chr(97 + i) for i in range(26)}
    mapeo[26] = ' '  # Agregar el espacio como un carácter alfabético
    # Convertir los números en caracteres usando el diccionario del alfabeto
    caracter = ''.join(mapeo[num] for num in matriz_apla1)
    print(caracter)
    return caracter


# Prueba Función:
# print(desc_final())

# ************************************************************************************************************** #
# P R O G R A M A   P R I N C I P A L
cif_final()
desc_final()
