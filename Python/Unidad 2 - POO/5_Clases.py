# ***************************************************************************************************************

# Resumen Python Aspectos básicos
# Version 0.0.0.0.0.0.1
# DonPollo 2024 - All rights reserved

#    P O O  /  C L A S E S


# ***************************************************************************************************************

#    I N T R O D U C C I O N :

# Es una función que permite conocer el tipo de dato en cuestión.

mensaje = "hola mundo"
print(type(mensaje))
# Imprime: " <class 'str'> "  Clase str = String. Pero además tambien pertenece a la "clase" string.

# Una clase es una estructura de programación que permite definir un conjunto de métodos y atributos que describen
# un objeto o una identidad. Las clases proveen una forma de empaquetar datos y funcionalidad juntos. Al crear
# una nueva clase, se crea un nuevo tipo de objeto, permitiendo crear nuevas instancias de ese tipo.
# Cada instancia de clase puede tener atributos adjuntos para mantener su estado. Las instancias de clase también
# pueden tener métodos (definidos por su clase) para modificar su estado.

# Clase: es el plano de construcción (por ejemplo, de una casa)
# Objeto: es la clase construida (por ejemplo, la casa en sí), a ello se le denomina una "instancia de una clase".
# Por tanto, la instancia corresponde a una casa en particular.

# Clase: Humano
# Objeto: Alejandro, Don Pollo, Etc... (individuos) o instancias de la clase humano.

# ***************************************************************************************************************

#   C R E A N D O   C L A S E S :

# Se crean con "class". Las clases se crean con mayúsculas en todas las palabras que incluyan y las funciones
# con minúsculas y "_" para los espacios.

# Luego se agregan todas las funciones y variables


class Perro:
    # Ya no se llaman funciones, si no métodos. El primer parámetro siempre es "self".
    def habla(self):
        print("Guau! " * 2)


# Para se llamar a la clase "Perro", se hace al igual que una función:
# Con la primera letra mayúscula, se puede diferenciar entre una funcion o una nueva instancia de una clase.
# Perro()

mi_perro = Perro()
print(type(mi_perro))
# Imprime:

# <class 'str'>
# <class '__main__.Perro'> ---> Esto indica el módulo en donde se está creando la instancia de "perro".


# Para llamar al método de habla:
mi_perro.habla()

# Para verificar si el objeto es instancia de alguna clase en particular:

# mi_perro es una instancia de la clase Perro.
print(isinstance(mi_perro, Perro))

# ***************************************************************************************************************

# C O N S T R U C T O R :

# Es una función que podemos definir dentro de cada una de las clases, ejecutándose siempre que se cree una nueva
# instancia de la clase. Se conoce como " __init__ ".
# Self es una pañabra reservada que se utiliza para referenciar las instancias de las clases. Va cambiando
# dependiendo de la instancia.


class Gata:  # Clase Gata
    # self: referencia a la clase, los demás son valores del constructor.
    def __init__(self, nombre, edad):
        self.nombre = nombre     # nombre: propiedad de la clase.
        self.edad = edad         # edad: propiedad de la clase.

    # Método. Se accede con "self". Es lo mismo que una función.
    def hablar(self):
        print(f"{self.nombre} dice: Miaaaushh!")


lucinda = Gata("Lucinda", 1)  # Instancia N°1
carmela = Gata("Carmela", 1)    # Instancia N°2

lucinda.hablar()

# ***************************************************************************************************************

# P R O P I E D A D E S    D E   C L A S E :
