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

primerset = {6, 7, 3, 9, 1, 0, 4}
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
# print(segundoset, tercerset)


