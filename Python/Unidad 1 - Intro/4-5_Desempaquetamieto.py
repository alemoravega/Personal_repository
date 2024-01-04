# *************************************************************************************************

print("""*Resumen Puthon Aspectos básicos*""")
# print(" ")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

#    D E S E M P A Q U E T A M I E N T O  :

# *************************************************************************************************

# Se utiliza para desempaquetar los valores de un iterable que aún no ha sido assignados a una llave
# en un diccionario o de una lista.
print("Operador Desempaquetamiento: * y **")
lista1 = [1, 2, 3, 4]
print("Sin operador *: ", lista1)
print("Con operador *: ", *lista1)

# Combinacion de listas:
print("Combinar listas: ")
lista2 = [5, 6, 7, 8]
listas1_2 = [lista1, lista2]
print("Sin operador *: ", listas1_2)
listas1_2 = [*lista1, *lista2]
print("Con operador *: ", listas1_2)

# Uso con diccionarios:
# se usa con **.

punto1 = {"x": 10}
punto2 = {"y": 15}
punto3 = {**punto1, **punto2}
print("Con ** se unen 2 listas, formando una nueva: ", punto3)

# Elemento repetidos en diccionarios.
print("Elementos repetidos")
punto1 = {"x": 10, "y": "DonPollo"}
punto2 = {"y": 15}
punto3 = {**punto1, **punto2}
print("Se mantiene el 'y': 15.", punto3)

# Para agregar propiedades a los diccionarios,
# utilizando ** :
print("Agregar propiedades al diccionarios")
punto1 = {"x": 10}
punto2 = {"y": 15}
punto3 = {**punto1, "DonPollo": 20, **punto2, "Es el mejor": 25}
print("Se agregan propiedades: ", punto3)
