# *************************************************************************************************

print("""*Resumen Puthon Aspectos básicos*""")
print(" ")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# L I S T A S .

# *************************************************************************************************

# Las listas son una sucesión de elementos, como listas (sublistas), números, strings, etc.
print("Ejemplos de Listas: ")
print(" ")
# lista con 10 elementos (números):
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista con 10 enteros: ")
print(lista1)
print(" ")
# lista con 3 elementos (strings):
lista2 = ["a", "b", "c"]
print("lista con 3 strings: ")
print(lista2)
print(" ")
# Lista con palabras (Strings):
lista3 = ["Don", "Pollo", "es", "el", "mejor"]
print("Lista con strings (palabras): ")
print(lista3)
print(" ")
# Lista con valores booleanos:
lista4 = [True, False, True,]
print("Lista con valores Booleanos: ")
print(lista4)
print(" ")
# Lista con listas (matriz):
print("Lista con sublistas: ")
lista5 = [["A", "B", "C"], [1, 2, 3], [True, False, False]]
print(lista5)
print(" ")
# Las listas pueden multiplicar sus elementos poniendo un * afuera de la lista:
lista6 = [0] * 10  # Números de veces a multiplicar.
print("Lista con un elemento multiplicado: ")
print(lista6)
print(" ")
# Con más elementos:
lista7 = [0, 1] * 10  # Números de veces a multiplicar.
print("Lista con varios elementos multiplicados: ")
print(lista7)
print(" ")
print(" o también con varias listas: ")
lista8 = [[0], [1], [2, 3]] * 5  # Números de veces a multiplicar.
print(" ")
print(lista8)
print(" ")
# Las listas se pueden juntar:
superlista = lista1 + lista2
print("Superlista (2 listas juntas) : ")
print("")
print("Lista 1 :", lista1)
print("Lista 2 :", lista2)
print("Listas 1 y 2: ", superlista)
print(" ")
# Lista que tenga un rango de números:
print("Lista con un rango de números usando range: ")
print("""Para ello se utiliza la siguiente sintaxis:
    rango = list(range(10))
    *Siendo el 10 el número de elementos requeridos.
""")
rango = list(range(10))
print(rango)
print(" ")
print("Segundo ejemplo de range: ")
print("""Para una lista con un rango de números determinado,
    se requiere la siguiente sintaxis:
    rango = list(range(5, 11))
    """)
rango1 = list(range(5, 11))
print(rango1)
print(" ")
