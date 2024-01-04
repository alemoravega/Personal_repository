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
            "Doña Carmela",  # 6
            "Don Pitufo",  # 7
            "Don Tobi",  # 8
            "Doña Emma"]  # 9

# Para agregar datos, método insert():

# el 1 significa el lugar en dónde se quiere insertar el elemento.
regalon2.insert(1, "Doña Kumi")

# Para agregar elementos al final del listado, método append():
regalon2.append("Doña Cuchi")

# Para eliminar elementos dentro de un listado, método remove():
regalon2.remove("Doña Kumi")  # Sólo borra el primero.
# Método pop(), borra el último elemento:
regalon2.pop()
# Si se requiere borrar un elemento con un indice en particular:
regalon2.pop(0)  # Se borra "Don Rex"
# otra forma de eliminar elementos, del .
del regalon2[0]  # Se borra "Don Brownie"
# Para borrar todo, método clear():
regalon2.clear()
print(regalon2)


# Cómo ordenar elementos de una lista.

numeros1 = [1, 56, 2, 56, 34, 87, 12, 73, 9, 99, 57, 35, 63, 37]
print(numeros1)
# Método sort(), para ordenar listas de menor a mayor:
numeros1.sort()
print(numeros1)
# Para ordenar la lista de mayor a menor:
numeros1.sort(reverse=True)
print(numeros1)


# Función sorted:
# Esto es una nueva lista ordenada de menor a mayor.
numeros2 = sorted(numeros1)
print(numeros2)

# Orden de listas que contienen listas.
# Con Id a la izquierda:
usuarios = [[5, "Don Pollo"], [1, "Doom Pollo"], [3, "Pollito"], [6, "Pollo"]]
usuarios.sort()  # ordena el listado de menor a mayor
print(usuarios)

# Con Id a la derecha:
usuarios = [["Don Pollo", 5], ["Doom Pollo", 1], ["Pollito", 4], ["Pollo", 6]]
usuarios.sort()
print()
# no ordena, porque debe tener algo ordenable a la izquierda.
# Se le debe pasar una función:


def ordena(elemento):
    """Funcion que ordena"""
    # por si mismo no ordena, se le deben pasar parámetros.
    return elemento[1]


# De esta forma, se ordena de menor a mayor con un índice en la derecha.
usuarios.sort(key=ordena)
# Para que sea de mayor a menor, se debe pasar otro argumento; reverse = True
usuarios.sort(key=ordena, reverse=True)
print(usuarios)

# Función lambda: Es una función anónima para extraer el segundo elemento
# Hace lo mismo que la anterior pero con una escritura mas sencilla:

usuarios.sort(key=lambda el: el[1], reverse=True)
# Lambda: se utiliza como una función anónima para extraer el segundo elemento
# Reverse: indica que la lista se debe ordenar en orden descendente
print(usuarios)


# Listas de compresión:

# Se usa lista "usuarios2":

usuarios2 = [["Don Pollo", 5], ["Doom Pollo", 1], ["Pollito", 4], ["Pollo", 6]]
# Obtener solo el nombre, no el identificador.
# Cómo ya se vió antes, se podría a través del método "for - in".

nombres = []
for regalo in usuarios2:
    nombres.append(regalo[0])

# Aqui se recorre cada "usuario" (elemento de la lista) en la lista "usuarios2", y toma el
# primer elemento (indice 0) de cada "usuario", creando una nueva lista llamada #nombres".
# La expresion es la siguiente:
# nombre_lista_nueva = [primer_elemento[0] for elementos in nombre_lista_original]
nombres = [usuario[0] for usuario in usuarios2]  # Nombre: map
# Cada elemento se transforma, en este caso accediendo al primer elemento.

# filtar - filter:
# En este ejemplo se filtraron elementos mayores a 2.
nombres = [usuario[0] for usuario in usuarios2 if usuario[1] > 2]

# map - filter
# Crear listas a partir de listas existentes, filtrar y transformar:
nombres = [usuario[0] for usuario in usuarios2 if usuario[1] > 2]
print(nombres)

# Función de Filter:

otros_usuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios2))
print(otros_usuarios)

# se puede usar map y filter en lugar de la compresión de listas, tienen el mismo resultado.
