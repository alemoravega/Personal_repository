# *************************************************************************************************

print("""*Resumen Puthon Aspectos básicos*""")
# print(" ")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

#   D I C C I O N A R I O S :

# *************************************************************************************************

# Son una colección de datos que se encuentran agrupados por una llave y un valor. La llave solo
# acepta strings, pero el valor puede ser cualquier tipo de dato.

# Ejemplo:

punto_a = {"x": 25, "y": 50}

# Se puede acceder a sus datos, solo mediante el string del valor requerido:
# print(punto_a["x"])
# print(punto_a["y"])

# Para agregar llaves:
punto_a["z"] = 75
print(punto_a)

# Si se trata de acceder a un elemento a través de una llave que no existe,
# dará un error: KeyError: 'llave'. Para solucionar el problema anterior, se tienen 2 alternativas:

# if:
# if "m" in punto_a:
# print("El valor de la consulta es: ", punto_a["m"])

# método get():
print(punto_a.get("m"))
print(punto_a.get("x"))
# Si encuentra la llave, retorna el valor.
# Si no encuentra la llave, retorna NONE.
# Además, si no se encuentra la llave, es posible pasarle un segundo argumento, para que devuelva la llave:
print(punto_a.get("m", 100))

# Para eliminar llave y su valor, se utiliza "del":
del punto_a["x"]
# Función del():
del (punto_a["y"])

punto_a["x"] = 25
punto_a["y"] = 50

# Interación con for, devuelve el nombre de las llaves pero no su valor.
for valor in punto_a:
    print(valor)
# Para ver su valor, método items().
for valor in punto_a.items():
    print(valor)

# Ejemplo de uso diccionarios Python.

