# -*- coding: utf-8 -*-

long = int(input("¿Longitud del tablero? "))
caracter = " "
contador = 0

for h in range(long):
    for i in range(3):
        if (h % 2) == 0:
            caracter = " "
        else:
            caracter = "*"

        for j in range(long * 3):
            print(caracter, end="")
            contador = contador + 1

            if (contador % 3) == 0:
                contador = 0

                if caracter == "*":
                    caracter = " "
                else:
                    caracter = "*"
        print()
    if caracter == "*":
        caracter = " "
    else:
        caracter = "*"
print()
