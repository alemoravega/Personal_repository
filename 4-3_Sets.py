# *************************************************************************************************

print("""*Resumen Puthon Aspectos básicos*""")
# print(" ")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

#   S E T S :

# *************************************************************************************************

# Son grupos o conjuntos de elementos (datos) que no se puede repetir y no tienen orden. Si re
# repiten elementos, python automáticamente los borra, como tambien las ordena de menor a mayor.
# Se utilizan "{}" para definirlas.

primerset = {6, 7, 3, 9, 1, 0, 4, 2}
# print: {0, 1, 3, 4, 6, 7, 9}

# Se puede agregar un elemento con el método add(), similar  al metodo append() para listas.
primerset.add(5)
# Método remove() para eliminar elementos:
primerset.remove(6)

# transformar una lista/tupla a un set utilizando el método set():
# lista:
segundoset = [3, 4, 5]
tercerset = (6, 7, 8)
# Método set() recbiendo un iterable:
segundoset = set(segundoset)
tercerset = set(tercerset)
print(segundoset, tercerset)

# operadores de sets.

# "|" : "operador union".
# Unión de sets (eliminando los elementos duoplicados y ordenándolos)
print(primerset | segundoset | tercerset)

# "&" : Intersección.
# Devuelve los elementos en común de los sets:
print(primerset & segundoset)
# {3, 4, 5}

# "-": Diferencia:
# Devuelve los elementos de 2 sets que se quitan del primer set:
print(primerset - segundoset)

# "^": diferencia simétrica:
# devuelve los elementos que se encuentran en ambos set que no se encuentren duplicados.
print(primerset ^ segundoset)

# El problema de los sets es que no se pueden acceder a sus datos de forma ordenada.
# Pero si se puede consultar la existencia de un elemento con un if:

if 5 in segundoset:
    print("Hay un 5 en este Set")
