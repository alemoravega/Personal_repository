# ********************************************************************************************

print(""" Resumen Puthon Aspectos básicos""")
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

# And: necesita que todas las evaluaciones sean True. Si la primera es False, la siguiente
# no se evaluará. Las evaluaciones se ejecutan de izquierda a derecha, a menos que exista
# un paréntesis.

# OR: si la primera evaluación es True, no se evaluarán las siguientes.

# ********************************************************************************************

# Cadena de Comparadores:

edad5 = 25

if 15 <= edad <= 65:
    print("Puedes entrar: ")

# ********************************************************************************************

# Loop for:

# Se utiliza para iterar una lista de elementos.
# RANGE: crea una lista de números y la devuelve. En este caso, range(5) es una lista que
# empieza en 0 al 4.
# La variable "número" va a tomar el valor de cada variable que se encuentre en la lista.
# Por lo tanto, el bucle se ejecutará por cada elemento.

for numero in range(5):
    print(numero)

# El primer argumento de range(x,y), "x" es el número en el cual se inicia la lista, y el "y",
# es el número de elementos que contendrá la lista numérica.

for numero in range(1, 5):
    print(numero)

# También se puede combinar con Strings: (solo acepta la *)

for numero in range(1, 5):
    print(numero * "¡Hola!")

# Si hay mas "print", se ejecutarán una a una de arriba a abajo, y luego pasará al sgte número:
for numero in range(1, 5):
    print("Las palabras se repetirán", numero, "veces.")
    print(numero * "¡Hola! ")
    print(numero * "¿Cómo estás? ")
    print(numero * "¡Responde mierda!")

# También se puede iterar Strings:
for char in "DonPollo":
    print(char)

# ********************************************************************************************

# For else:

# En este ejemplo, se utiliza para buscar un dato númérico.

# buscar = int(input("Ingresa un número: "))
buscar = 9
for numero1 in range(10):
    # Se usa para ver todo lo que recorre el loop o cuántas veces se ejecuta.
    print(numero1)
    if numero1 == buscar:
        print("Encontré el número", 9)  # Se puede cambiar por "buscar"
        break  # BREAK: termina el programa una vez se cumple la condición.
else:  # Se utiliza como "for else", en casos que no se encuentra el valor.
    print("No se encontró el número buscado")

# ********************************************************************************************

# While:

# El bucle se ejecuta mientras se cumpla la condición.

numero = 1
while numero < 10:
    print(numero)
    numero *= 2

# Ejemplo para salir de una aplicación:
comando = "salir"
while comando.lower() != "salir":
    comando = input("$. ")
    print(comando)

# Loop infinitos, se da cuando no se tiene una condición de salida.

# ********************************************************************************************

# Loops anidados: son loops dentro de un loop.

for j in range(3):       # Outer loop
    for k in range(3):   # inner loop
        print(f"{j}, {k}")

for j in range(2):
    for k in range(2):
        for l in range(2):
            for m in range(2):
                print(f"{j}, {k}, {l}, {m}")

# ********************************************************************************************
