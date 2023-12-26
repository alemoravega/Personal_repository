# ********************************************************************************************

""" Resumen Puthon Aspectos básicos"""
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

# F L U J O S :  I F, F O R, W H I L E, E T C.

# ********************************************************************************************

# if, elif y else.

# Condicional if: si se cumple la condición, se ejecuta x que esté anidado, si no se cumple,
# se ejecuta lo demás. El orden de las instrucciones es importante.

edad = int(input("¿Cuántos años tienes? "))
if edad > 18:
    print("Eres mayor de edad.")
elif edad == 18:
    Print("Tienes justo 18, eres mayor de edad.")
else:
    print("Eres menor de edad")

# If Ternario

# Otra forma de escribir los if y else:
edad1 = int(input("Ingresa tu edad: "))
mensaje1 = "es mayor de 17" if edad1 > 17 else "es menor"
print(mensaje1)

# ********************************************************************************************
