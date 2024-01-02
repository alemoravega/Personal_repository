# *************************************************************************************************

print("""*Resumen Puthon Aspectos básicos*""")
# print(" ")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

#   T U P L A S:

# *************************************************************************************************

# Es lo mismo que una lista, pero no se puede modificar en lo absoluto.
# se utilizan con "()" a diferencia de las listas que se utilizan con "[]".

numeros = (1, 2, 3, 4, 5)

# Pueden concadenarse:

numeros1 = (1, 2, 3, 4, 5) + (6, 7, 8, 9)


# Para transformar una lista a una tupla, se hace mediante la funcion "tuple()".
# Dicha función puede recibir cualquier cosa que sea iterable; como un string

punto = [1, 2]
punto1 = tuple(punto)
# tambien se puede pasar los argumentos como enteros:
punto2 = tuple([1, 2, 3])

# las funciones "append()" [agrega elementos al final de la lista]
# y "pop()"" [eliminar el elemento final de la lista] no pueden ser ejecutadas en tuplas.

# numeros1[0] = 5
# marca error, porque no se pueden modificar.

# Desempaquetamiento de Tuplas:
primero, segundo, *otros = numeros1

# iteración de tuplas:
# for n in numeros1:
# print(n)

# Finalmente, para modificar una tupla, se debe convertir a una lista con la función "list()":

# la tupla "numeros1" se convierte a una lista denominada "listanumeros":
listanumeros = list(numeros1)
# Luego, se edita la lista:
listanumeros[0] = 0
