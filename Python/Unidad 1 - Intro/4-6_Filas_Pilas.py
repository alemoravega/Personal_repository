# ***************************************************************************************************************
from collections import deque

print("""*Resumen Puthon Aspectos básicos*""")
# print(" ")
# Version 0.0.0.0.0.0.1
# DonPollo 2023 - All rights reserved

#    F I L A S   Y   P I L A S :

# ***************************************************************************************************************

# Una fila son first in, first out. El primero que llega, es el primero que se va.
# Si se requiere quitar un elemento, el primero en quitarse deberia ser "1" porque esta al principio de la lista.
# Pero en python si se quita un elemento de la lista, los demás restantes avanzan un lugar, lo que puede ser
# muy demandante para los recursos del sistema.

# Para ello se importa el siguiente módulo:
# "deque" es una clase.

# from collections import deque

fila = deque([1, 2, 3])
print("Lista original: ", fila)

# Si se quisiera pasar mas elementos al la lista "fila", se puede utilizar el método 'append()':
fila.append(4)
fila.append(5)
fila.append(6)
print("Lista con elementos agregados: ", fila)

# Para eliminar elementos que se tienen a la izquierda de la fila se utiliza el módulo 'popleft()':
fila.popleft()
print("Lista sin el primer elemento de izq a der: ", fila)

# Para determinar si la fila se encuentra vacía:
# (una lista vacía corresponde a 'Falsey', que son todos los que se evalúan como False.)
# (los valores que se evaluan como False son: string vacío, False, lista vacio y valores de 0.0)

fila1 = deque([1])
print(fila1)
# Se elimina el único elemento de la fila:
fila1.popleft()
if not fila1:
    print("La fila está vacía.")

# ***************************************************************************************************************

# Pilas: Una pila (también conocida como “stack”) es una estructura de datos en Python que permite almacenar y
# recuperar datos1. La característica principal de una pila es que sigue el principio de LIFO (Last In, First Out),
# lo que significa que el último elemento que se añade a la pila es el primero en ser eliminado.

# Lista Vacia:
pila = []
# Se agregan elementos:
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
# Con el modulo poop() se visualiza el último elemento de la lista:
ult_pila = pila.pop()
print(ult_pila)

# Para implementar una "pila", es necesario trabajar solo con los módulos append() y pop().

# Pila Vacía:
pila_vac = ()
if not pila_vac:
    print("pila vacía")
