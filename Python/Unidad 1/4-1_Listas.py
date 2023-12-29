# *************************************************************************************************

print("""*Resumen Puthon Aspectos básicos*""")
# print(" ")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# L I S T A S .

# *************************************************************************************************

# Las listas son una sucesión de elementos, como listas (sublistas), números, strings, etc.
# print("Ejemplos de Listas: ")
# print(" ")
# lista con 10 elementos (números):
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Lista con 10 enteros: ")
# print(lista1)
# print(" ")
# lista con 3 elementos (strings):
lista2 = ["a", "b", "c"]
# print("lista con 3 strings: ")
# print(lista2)
# print(" ")
# Lista con palabras (Strings):
lista3 = ["Don", "Pollo", "es", "el", "mejor"]
# print("Lista con strings (palabras): ")
# print(lista3)
# print(" ")
# Lista con valores booleanos:
lista4 = [True, False, True,]
# print("Lista con valores Booleanos: ")
# print(lista4)
# print(" ")
# Lista con listas (matriz):
# print("Lista con sublistas: ")
lista5 = [["A", "B", "C"], [1, 2, 3], [True, False, False]]
# print(lista5)
# print(" ")
# Las listas pueden multiplicar sus elementos poniendo un * afuera de la lista:
lista6 = [0] * 10  # Números de veces a multiplicar.
# print("Lista con un elemento multiplicado: ")
# print(lista6)
# print(" ")
# Con más elementos:
lista7 = [0, 1] * 10  # Números de veces a multiplicar.
# print("Lista con varios elementos multiplicados: ")
# print(lista7)
# print(" ")
# print(" o también con varias listas: ")
lista8 = [[0], [1], [2, 3]] * 5  # Números de veces a multiplicar.
# print(" ")
# print(lista8)
# print(" ")
# Las listas se pueden juntar:
superlista = lista1 + lista2
# print("Superlista (2 listas juntas) : ")
# print("")
# print("Lista 1 :", lista1)
# print("Lista 2 :", lista2)
# print("Listas 1 y 2: ", superlista)
# print(" ")
# Lista que tenga un rango de números:
# print("Lista con un rango de números usando range: ")
print("""Para ello se utiliza la siguiente sintaxis:
rango = list(range(10))
# * Siendo el 10 el número de elementos requeridos.
""")
rango = list(range(10))
# print(rango)
# print(" ")
print("""Para una lista con un rango de números determinado,
se requiere la siguiente sintaxis:

    rango = list(range(5, 11))
""")
rango1 = list(range(5, 11))
# print(rango1)
# print(" ")
# Lista desde una cadena de caracteres:
print("""Para una lista con elementos de un strings,
se requiere la siguiente sintaxis:

    rango = list("Don Pollo")
""")
rango2 = list("Don Pollo")
# print(rango2)
# print(" ")


# Manipulando las listas:

regalones = ["Don Rex", "Don Brownie",
             "Doña Dora", "Doña Carmela", "Doña Lucinda"]
# Para acceder a un elemento de las listas, se debe indicar el índice del elemento requerido:
# print("Lista Regalones:", regalones)
# Donde uno es el segúndo elemento, porque parte de 0.
# print("El segundo elemento de la lista \"Regalones\" es:", regalones[1])

# Para cambiar elementos del listado:
regalones[0] = "Laika"
print("""
Se cambia el elemento "Don Rex" por "Laika": 
""", regalones)

# Para obtener una parte determina de la lista:
# El primer número es de donde emnpieza y el segundo es donde termina.
print(regalones[1:3])
# Si se omite el primer elemento, empieza desde 0:
print(regalones[:3])
# Si se omite el último elemento, imprime hasta el final de la lista:
print(regalones[1:])
# Si se utiliza un número en el indice que es negativo, se cuenta desde la derecha.
print(regalones[-1])
# Para seleccionar elementos variados en la lista:
numeros = list(range(21))
# Range permite seleccionar el inicio de la lista:
numeros = list(range(5, 21))  # --> Empieza desde el número 5.
# Números pares:
print(numeros[::2])
# Números impares:
print(numeros[::3])
# Números multiplos de 4 y etc:
print(numeros[::4])
# Números multiplos de 5 desde el número 10:
print(numeros[10::5])


# Desempaquetando listas:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# de esta forma se puede asignar nombre a los elementos de la lista:
# *otros: Para empaquetar en una lista distinta:
primero, segundo, tercero, *otros = numeros
# print(primero)  # 1
# print(segundo)  # 2
# print(tercero)  # 3
# print(primero, tercero)
primero, segundo, *otros, penultimo, ultimo = numeros
# imprime el elemento primero y los elementos restantes.
# print(primero, otros)
# imprime el elemento primero, el ultimo y el resto.
# print(primero, otros, ultimo)
# print(segundo, ultimo)


# Iterando listas:
# Iterable: que se puede repetir (Método iter), pudiendo tomar índices consecutivos empezando desde 0.

regalon1 = ["Don Rex", "Don Brownie", "Doña Laika",
            "Doña Dora", "Doña Carmela", "Doña Lucinda", "Doña Carmela"]
for regalon in regalon1:
    print(regalon)

# ¿Cómo se puede acceder al índice de los elementos que estamos iterando?
for indice, regalon in enumerate(regalon1):
    print(indice, regalon)  # Tuplas


# Buscar elementos en una lista: método "index()".

if "Doña Carmela" in regalon1:
    print(regalon1.index("Doña Carmela"))
    # Devuelve 4, que es el lugar en donde el elemento se encuentra.

# Se utiliza el método "count()" que retorna el número de veces
# que se repite el elemento en la  lista.
print(regalon1.count("Doña Carmela"))

# Agregando y eliminando elementos de una lista.

regalon2 = ["Don Rex",  # 0
            "Don Brownie",  # 1
            "Doña Laika",  # 2
            "Doña Dora",  # 3
            "Doña Pitufa",  # 4
            "Doña Lucinda",  # 5
            "Doña Carmela"  # 6
            "Don Pitufo",  # 7
            "Don Tobi",  # 8
            "Doña Emma"]  # 9

# Para agregar datos, método insert()
