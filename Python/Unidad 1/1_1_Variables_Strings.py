

""" Resumen Puthon Aspectos básicos"""
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# V A R I A B L E S : S T R I N G S

# *********************************************************

# Funcion Print
# inprime en pantalla

print("print es la función básica")

# Para imprimir más veces la variable se usa el multiplicador * seguido del número de veces a repetir:

print("print es la funcion básica " * 4)

# *********************************************************

# Tipos / Variables Básicos
# las variables en Python son sensibles a las maysculas y minúsculas.

donpollo1 = "ejemplo1"  # str = String
donpollo2 = "1000"  # int = Entero
donpollo3 = "9.9"  # float = Decimales
donpollo4 = "True"  # Buleano - True: T siempre en mayúscula
donpollo5 = "False"  # buleano - False: F siempre en mayuscula

print(donpollo1, donpollo2, donpollo3, donpollo4, donpollo5)

# *********************************************************

# Strings
# Uso de comillas simples y triples.

donpollo = "¡Hola! ¿Cómo estás?"
ejemplo = """ 
Usando las 3 comillas
la impresión respeta
el orden del texto
"""

print(donpollo, ejemplo)

# *********************************************************

# Strings / Función len
# Permite conocer la longitud de un string en particular.
# En este caso lo que está entre paréntesis se denomina Argumento.

len(donpollo)

# Para imprimir el valor, se escribe así:

print(len(donpollo))

# Para acceder a un carácter en párticular se usan [], donde van 2 índices.
# El primer se usa para acceder a la primera letra (Primer carácter siempre es 0):

print(donpollo[0])

# Al poner : el primer número significa desde donde se va a imprimir y el segundo dígito hasta donde:

print(donpollo[0:3])

# Con el solo valor de la izq, sin el de la derecha, se rellena el valor con todo el ultimo caracter del
# valor del string

print(donpollo[8:])

# con el valor de la derecha, parte desde el primer carácter del valor del string:

print(donpollo[:8])

# Cuando no tiene ningún valor, genera una copia completa :

print(donpollo[:])

# *********************************************************

# Strings / Formato
# Operador concadenación. Se usa para unir variables.
# Se debe usar con " " para generar espacios entre variables.

nombre = "Alejandro"
sobrenombre = '"Don Pollo"'
apellido = "Mora"
nombre_completo = nombre + " " + sobrenombre + " " + apellido
print(nombre_completo)

# Sin embargo, para formatear ahora se utiliza f seguido de "" mas {}, dentro de ella se agrega la variable:

nombre_completo1 = f"{nombre} {sobrenombre} {apellido}"

print(nombre_completo1)

# Además, dentro de {}, se pueden agregar todo tipo de funciones y operaciones:

nombre_completo2 = f"{nombre[7]} {(25.4+34)/3}"

print(nombre_completo2)

# *********************************************************

# Strings / Métodos
# Los métodos son funciones dentro de los objetos, es decir,
# les agrega carácteristicas al valor de la variable.

regalon = " Don Rex es el mejor! "


# upper = transforma el string en letras mayúsculas.
print(regalon.upper())

# lower = transforma el string en letras minúsculas.
print(regalon.lower())

# capitalize = deja la primera letra del string en mayúscula y las demás en minúscula.
print(regalon.capitalize())

# title = La primera letra de cada palabra del string queda en mayúscula.
print(regalon.title())

# strip = elimina los espacios de la izquierda y de la derecha.
print(regalon.strip())

# lstrip = elimina el espacio de la izquierda.
print(regalon.lstrip())

# rstrip = elimina el espacio de la derecha.
print(regalon.lstrip())

# Se pueden encadenar los métodos.
print(regalon.strip().capitalize())

# find = busca la cadena de caracteres que se le indique y devuelve el índice,
# un número que indica desde donde comienza la o las letras seleccionadas.
# Cuenta los espacios como caracter. Si devuelve -1, es que no encontró el caracter.
print(regalon.find("e"))
print(regalon.find("on R"))

# replace = reemplaza el caracter por una seleccionada. Necesita siempre 2 argumentos.
print(regalon.replace("el mejor", "hediondo pero regalón"))

# in = devuelve Boolean (True o False) dependiendo el argumento dado.
print("Rex" in regalon)
print("flojo" in regalon)

# not in = devuelve Boolean (True o False) dependiendo el argumento dado.
print("Rex" not in regalon)
print("flojo" not in regalon)

# *********************************************************

# Strings / Secuencias de Escape.
# Uso de Comillas Simples y Dobles para que aparezcan en pantalla:

# " " entre '' y visceversa:
ejem_sec_esc = "'DonPollo' es el mejor"
ejem_sec_esc1 = '"DonPollo" es el mejor'
print(ejem_sec_esc)
print(ejem_sec_esc1)

# \" para comillas dobles:
ejem_sec_esc2 = '\"DonPollo\" es el mejor'
print(ejem_sec_esc2)

# \' para comilla simples:
ejem_sec_esc3 = "\'DonPollo\' es el mejor"
print(ejem_sec_esc3)

# \\ Para BackSlash:
ejem_sec_esc4 = "\\DonPollo\\ es el mejor"
print(ejem_sec_esc4)

# \n Nueva Línea:
ejem_sec_esc5 = "DonPollo \nes el \nmejor"
print(ejem_sec_esc5)

# *********************************************************
