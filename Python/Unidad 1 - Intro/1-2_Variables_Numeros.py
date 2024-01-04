# ********************************************************************************************

""" Resumen Puthon Aspectos básicos"""
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# V A R I A B L E S :   N Ú M E R O S

# ********************************************************************************************

# Pueden ser de varios tipos:

import math
numero = 2               # Entero -> integer - int
decimal = 1.2            # Decimal -> float
imaginario = 2 + 2j      # Número imaginario, no existe.
# Ejemplo: 2 + 2i -> i significa la raíz cuadrada de -1.
# En python se utiliza 'j' y en matemáticas se utiliza 'i'.

print(numero)
print(decimal)
print(imaginario)

# ********************************************************************************************

# Operaciones:

# Suma:
print(9 + 3)
# Resta:
print(9 - 3)
# Multiplicación:
print(9 * 3)
# División:
print(9 / 3)
print(9 // 3)  # (si no se quieren los decimales, se utiliza //)
# Módulo, que es el resto del resultado de la división.
# En este ejemplo, 8 se divide en 3 partes iguales, sobrando 2:
print(8 % 3)
# Si se divide el 3 en 8 partes, resultará 0.375.
print(3 / 8)
# Con mod, dará 3, que es lo que sobra.
print(3 % 8)
# Número elevado a, donde 6 es la base y 2 es el exponente:
print(6 ** 2)

# ********************************************************************************************

# Reemplazar variables por sí mismas:

numero1 = 5
print(numero1)
# A la variable se le suma 2 y reemplaza su valor primario.
numero1 = numero1 + 2
print(numero1)
# Una mejor forma de hacer lo anterior:
numero2 = 10
numero2 += 2
print(numero2)
# se pueden hacer con todos los operadores.
# ********************************************************************************************
# Funciones integradas:

# Round redondea al número más cercano:

# Con números:
print(round(1.945324))
# Redondea con 1 decimal:
print(round(1.945324, 1))
# Redondea con 2 decimales:
print(round(1.945324, 2))

# Con variables:
numero3 = 4.36930
# Redondea al número 4.
print(round(numero3))
# Redondea con 1 decimal
print(round(numero3, 1))
# Redondea con 2 decimales
print(round(numero3, 2))
# Redondea con 3 decimales:
print(round(numero3, 3))


#  Abs: Entrega el valor absoluto (positivo) de un número.

numero4 = -5
print(abs(numero4))

# ********************************************************************************************

# M Ó D U L O S  :  M A T H

# ********************************************************************************************

# Los módulos son archivos escritos que se pueden traer y vienen escritos en Python para
# no tener que escribirlos de nuevo.


# Math es un archivo que contiene código escrito.

# Ceil es un método que lleva un número al entero más cercano hacia arriba:
print(math.ceil(1.276554467))
# Floor es un método que lleva un número al entero más cercano hacia abajo:
print(math.floor(1.256564576))
# Isnan es un método que retorna false si el valor que se le está entregando es un número.
print(math.isnan(34))
# pow es iun metodo que permite elevar un numero a la potencia requerida:
# (El primer número es la base y el segundo es el exponente)
print(math.pow(10, 4))
# sqrt: retorna la raíz cuadrada de un número.
print(math.sqrt(9))


# La documentación completa se encuentra en:
# https://docs.python.org/3/library/math.html

# ********************************************************************************************
