# ********************************************************************************************

print(""" Resumen Puthon Aspectos básicos""")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# F U N C I O N E S .

# ********************************************************************************************

# Funciones: Son bloques de codigo que pueden ser llamados por el usuario


def funcion1():           # Definición de la función / nombre / argumentos.
    print("DonPollo")
    print("Es el mejor")


funcion1()  # Llamar a la función

# Argumentos y parámetros:


def funcion2(adjetivo):
    print("DonPollo")
    print(f"Es el {adjetivo}")


funcion2("peor")  # Llamar a la función con el argumento dado.
funcion2("mas brigido!")
# Cuando se hace referencia a una variable dentro de una función, se dice que se hace uso
# de sus parámetros. En la función2, el parametro es "adjetivo". Por el contrario, cuando se
# llama a la función, el valor se denomina argumento, por ejemplo: "peor".

# Función con mas de un parámetro:


def funcion2(adjetivo1, adjetivo2):
    print("DonPollo")
    print(f"Es el más {adjetivo1}, y también el mas {adjetivo2}")


funcion2("pulentamente", "rico")
