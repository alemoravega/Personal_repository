# *************************************************************************************************

print(""" Resumen Puthon Aspectos básicos""")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# F U N C I O N E S .

# *************************************************************************************************

# Funciones: Son bloques de codigo que pueden ser llamados por el usuario


def funcion1():
    """Definición de la función / nombre / argumentos."""
    print("DonPollo")
    print("Es el mejor")


funcion1()  # Llamar a la función

# Argumentos y parámetros:


def funcion2(adjetivo):
    """Segundo ejemplo"""
    print("DonPollo")
    print(f"Es el {adjetivo}")


funcion2("peor")  # Llamar a la función con el argumento dado.
funcion2("mas brigido!")

# Cuando se hace referencia a una variable dentro de una función, se dice que se hace uso
# de sus parámetros. En la función2, el parametro es "adjetivo". Por el contrario, cuando se
# llama a la función, el valor se denomina argumento, en este caso por ejemplo el argumento
# es: "peor".

# Función con más de un parámetro:


def funcion21(adjetivo1, adjetivo2):
    """Tecer ejemplo"""
    print("DonPollo")
    print(f"Es el más {adjetivo1}, y también el más {adjetivo2}")


funcion21("pulentamente", "rico")

# si no hay algún argumento, da error por lo que puede establecer un argumento por defecto:


def funcion3(adjetivo3, adjetivo4="parámetro por defecto"):
    """Cuarto ejemplo"""
    print("DonPollo")
    print(f"Es el más {adjetivo3}, y también el más {adjetivo4}")


# Aquí hay un solo argumento:
funcion3("longi",)

# Aquí hay dos argumentos:
funcion3("tulón", "pichulero")

# Se puede nombrar los argumentos para determinar su posición en la función:

funcion3(adjetivo4="pichulero", adjetivo3="tulón")

# Múltiples argumentos en una función, el uso de xargs:
# permite tener todos los argumentos deseados al llamar una función:


def suma(*numeros):
    """ El * convierte el parametro en iterable, que toma todos los argumentos, con un for."""
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)  # Esta identación se debe poner así.


# Ejemplos de llamado a la función:
suma(1, 2)
suma(1, 2, 3)
suma(1, 2, 3, 4)
suma(1, 2, 3, 4, 5)

# Keywords Arguments - KWARGS : Crea diccionarios, pasando todos los argumentos que se requieran.


def get_product(**datos):
    """Ejemplo de ingreso de productos"""
    print(datos)


# Valor a la izq, es el nombre del parámetro.
# # Valor a la der, es el argumento.
get_product(id="0001-1", name="PC", desc="PC entero pulento")

# Para ingresar a argumentos específicos:


def get_product1(**datos1):
    """Ejemplo de ingreso de productos"""
    print(datos1["name"], datos1["id"])


get_product1(id="0001-1", name="PC", desc="PC entero pulento")

# Función return:


def suma_1(a, b):
    """función que ejemplifica return"""
    resultado = a + b
    return resultado  # Retorna la variable 'resultado', que es a + b.


# Se llama a la función:
C = suma_1(1, 2)
D = suma_1(C, 3)
print(D)
