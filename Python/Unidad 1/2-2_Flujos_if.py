# ********************************************************************************************

""" Resumen Puthon Aspectos básicos"""
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# F L U J O S :  I F, F O R, W H I L E, E T C.

# ********************************************************************************************

# if, elif y else.

# Condicional if: si se cumple la condición, se ejecuta x que esté anidado, si no se cumple,
# se ejecuta lo demás. El orden de las instrucciones es importante.

edad = 16
if edad > 18:
    print("Eres mayor de edad.")
elif edad == 18:
    Print("Tienes justo 18, eres mayor de edad.")
else:
    print("Eres menor de edad")

# If Ternario

# Otra forma de escribir los if y else:
edad1 = 16
mensaje1 = "es mayor de 17" if edad1 > 17 else "es menor de 17"
print(mensaje1)

# ********************************************************************************************

# Operadores Lógicos: and, or, not:

# AND: Cuando se tiene 2 condiciones y ambos son true, la operación completa es True. Si una
# es falsa, la operación completa es Falsa. OR: cuando una de las condiciones es True, la
# operación completa es True. Si ambas son verdaderas, la operación es falsa. NOT: niega el
# resultado de la operación.


# Ejemplo AND:
gas = True
encendido = True
if gas and encendido:
    print("Puedes avanzar!")

gas = True
encendido = False
if gas and encendido:
    print("Puedes avanzar!")
else:
    print("No puedes avanzar!")

# Ejemplo OR:

gas = True
encendido = False
if gas or encendido:
    print("Puedes avanzar!")
else:
    print("No puedes avanzar!")

gas = False
encendido = False
if gas or encendido:
    print("Puedes avanzar!")
else:
    print("No puedes avanzar!")

# Ejemplo NOT - OR:

gas = False
encendido = False
if not gas or encendido:
    print("Puedes avanzar!")
else:
    print("No puedes avanzar!")

# Ejemplo IF, AND:

gas = True
encendido = True
edad2 = 18

if gas and encendido and edad2 > 17:
    print("Puedes manejar")

# Ejemplo IF, AND, OR:

gas = True
encendido = True
edad2 = 16

if gas and encendido or edad2 > 17:
    print("Puedes manejar también")

# Ejemplo IF, AND, OR y NOT:

gas = False
encendido = True
edad3 = 16

if not gas and encendido or edad3 > 17:
    print("Puedes manejar también jeje")

# ********************************************************************************************

# Operaciones de corto circuito.
