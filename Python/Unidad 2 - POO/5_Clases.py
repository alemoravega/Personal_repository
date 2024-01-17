# ***************************************************************************************************************

# Resumen Python Aspectos básicos
# Version 0.0.0.0.0.0.1 - 1
# DonPollo 2024 - All rights reserved.

#    P O O  /  C L A S E S


# ***************************************************************************************************************

#    I N T R O D U C C I Ó N :

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
    patas = 4
    # self: referencia a la clase, los demás son valores del constructor.

    def __init__(self, nombre, edad):
        self.nombre = nombre     # nombre: propiedad de la clase (atributos).
        self.edad = edad         # edad: propiedad de la clase (atributos).

    # Método. Se accede con "self". Es lo mismo que una función.
    def hablar(self):
        print(f"{self.nombre} dice: Miaaaushh!")


lucinda = Gata("Lucinda", 1)  # Instancia N°1
carmela = Gata("Carmela", 1)    # Instancia N°2

lucinda.hablar()

# ***************************************************************************************************************

# P R O P I E D A D E S    D E   C L A S E   E   I N S T A N C I A S:

# las propiedades de las instanias de las clases se denominan "atributos".
# Los atributos se pueden modificar como cualquier variable, pero el cambio desde una instancia en particular,
# funciona para esa misma instancia y no para la clase.

# Desde la clase:
print(Gata.patas)
# Desde la instancia "lucinda" y "carmela":
print(lucinda.patas)
print(carmela.patas)
# Despues de definir el valor del atributo de la clase, se puede cambiar el valor de la variable patas.
Gata.patas = 3
# Desde la clase:
print(Gata.patas)
# Desde la instancia "lucinda":
print(lucinda.patas)
# Pero si se cambia desde la instancia en particular, sólo dicha instancia se verá afectada y no de todas las
# instancias de la clase:
carmela.patas = 4
print(lucinda.patas)
print(carmela.patas)

# ***************************************************************************************************************

# M É T O D O S   D E   C L A S E :


class Regalones:
    """Clase Regalones"""
    patas = 4  # Este atributo está asociado a la clase "Regalones" y a todas sus instancias.

    def __init__(self, nombre, edad):
        self.nombre = nombre     # nombre: propiedad de la clase (atributos).
        self.edad = edad         # edad: propiedad de la clase (atributos).

# Se puede tranformar este método como propio de la clase "Regalones":
    @classmethod
    def hablar(cls):
        """Función de ejemplo"""
# cls : convencion que se utiliza cuando se está creando métodos de clase para referirse a la clase misma.
# En este caso, es lo mismo que se escribiera "Regaloones".
        print("Ellas dicen: Miaaaushh!")


Regalones.hablar()

gata1 = Regalones("Lucinda", 1)      # Instancia N°1
gata2 = Regalones("Carmela", 1.5)    # Instancia N°2
perro1 = Regalones("Rex", 11)        # Instancia N°3

# Factory Method: Es una interfaz para crear un objeto, pero deja que sean las subclases quienes decidan
# qué clase instaciar. Ejemplo:


class Familia:
    def __init__(self, nombre, edad, parentesco):
        self.nombre = nombre
        self.edad = edad
        self.parentesco = parentesco

    @classmethod
    def factory(cls):
        return cls("DonPollo", 35, "hermano")


familiar1 = Familia.factory()
print(familiar1.edad, familiar1.nombre)


# Ejemplo de Factory Method de Bing:


class Animal:
    def hablar(self):
        pass


class Perro1(Animal):
    def hablar(self):
        return "Guau!"


class Gato1(Animal):
    def hablar(self):
        return "Miau!"


# class AnimalFactory:


    def create_animal(self):
        tipo = input("¿Qué tipo de animal quieres crear? ")
        if tipo.lower() == "perro":
            return Perro1()
        elif tipo.lower() == "gato":
            return Gato1()
        else:
            raise ValueError("Tipo de animal no soportado")


# Uso del Factory Method
# factory = AnimalFactory()
# animal = factory.create_animal()
# print(animal.hablar())


# ***************************************************************************************************************

# P R O P I E D A D E S   Y   M É T O D O S   P R I V A D O S:

# Una propiedad privada es una variable que solo puede ser accedida o modificada dentro de la misma clase
# donde fue declarada. De la misma manera, un método privado es una función que solo puede ser llamada desde
# otros métodos que pertenecen a la misma clase.

class Wwe:
    """ Se está definiendo una clase "Wwe" """

    def __init__(self, nombre, frase, finisher):
        # Método constructor de una clase, acepta 3 argumentos: nombre, frase, finisher.
        self.__nombre = nombre      # Para que sea privada se le pone: "__".
        self.frase = frase          # Propiedades públicas de la clase que se inicializan
        self.finisher = finisher    # con los valores de los argumentos.

    def habla(self):
        """Método público de la clase que imprime una frase"""
        print(f"{self.__nombre} dice: {self.frase}")

    @classmethod
    def factory(cls):
        """Método de clase que crea y devuelve una nueva instacia"""
        return cls("The Rock", "If you smeeeeell what The Rock... is cocking.", "Rock Bottom")

    def get__nombre(self):
        return self.__nombre


personaje1 = Wwe.factory()
personaje1.habla()
# Cambiar "nombre" a "__nombre", se usa 'Ctrl + Shift + p', luego "rename".

# Con "__" no se puede aceder al valoor del argumento:
# print(personaje1.__nombre)
# imprime lo siguiente:
# AttributeError: 'Wwe' object has no attribute '__nombre'.

# Método que permite devolver el valor del atributo privado pero no cambiar:

# def get__nombre(self):
#    return self.__nombre
# Ejemplo:

print(personaje1.get__nombre())     # Se obtiene el valor de la variable.

# Método set para cambiar un argumento.

# Explicación de Bing: *****************************************************************************************

# Los métodos privados en Python son funciones que solo pueden ser llamadas desde otros métodos que pertenecen
# a la misma clase. Python no distingue entre métodos públicos y privados de forma nativa, pero como convención,
# se prefija un guión bajo para indicar que un método debería ser interpretado como privado.


class MiClase:
    def __init__(self):
        self._atributo_privado = 1

    def _metodo_privado(self):
        print("Hola mundo!")


mi_objeto = MiClase()

# En este código, _metodo_privado es un método privado. Aunque técnicamente puede ser accedido fuera de la clase
# (como se muestra en el ejemplo), la convención es que solo debe ser utilizado dentro de la clase. Es importante
# mencionar que los métodos “privados” generalmente no están documentados y no se adhieren a ningún programa de
# retrocompatibilidad. Por esta razón, no es recomendable hacer uso de ellos fuera de la clase o módulo en el
# que están definidos.

# ***************************************************************************************************************

# D E C O R A D O R    P R O P E R T I E S :


class DonPollo:
    """ejemplo"""

    def __init__(self, nombre):
        self.nombre = nombre


pollo = DonPollo("Alejandro")
print(pollo)

# Lo anterior imprime:
# <__main__.DonPollo object at 0x00000119135A9BE0>
# __main__: Esto indica que la clase DonPollo está definida en el script principal (o módulo principal) que se está ejecutando.
# DonPollo: Este es el nombre de la clase del objeto.
# object at 0x00000119135A9BE0: Esto indica que el objeto está ubicado en la dirección de memoria 0x00000119135A9BE0.

# Para prevenir errores al asignar valores a los argumentos:

# El decorador @property en Python es un decorador incorporado que se utiliza para asignar funcionalidad “especial” a ciertos métodos
# para que actúen como getters, setters o deleters al momento de definir y usar propiedades en una clase.

# Aquí tienes un ejemplo de cómo se usa:


class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo

# En este código, mi_atributo es un método que se comporta como una propiedad gracias al decorador @property.
# Aunque técnicamente puede ser accedido fuera de la clase, la convención es que solo debe ser utilizado
# dentro de la clase12. Las propiedades se pueden considerar como la forma “Pythonica” de trabajar con atributos
# y programación orientada a objetos en Python porque permiten acceder
# al valor de los atributos de instancias como si fueran atributos públicos y usar la magia de los intermediarios (getters y setters)
# para validar valores nuevos y para evitar acceder o modificar los valores directamente.
# Además, al definir la propiedad con @property, el acceso a ese atributo se realiza a través de una función, siendo por lo tanto un
# acceso controlado2. Esto puede ser importante con ciertas variables que no queremos que sean accesibles desde el exterior de una
# manera no controlada.

# # *************************************************************************************************************************************

# M É T O D O S   M Á G I C O S :

# Son metodos que se ejecutan sin ser llamados directamente, se ejecutan de manera indirecta. Todos comienzan con __ al inicia y al final.


class Hediondos:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Hediondo: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} tiene {
            self.edad} año/s y dice que lo alimentes!!!")


gatuna1 = Hediondos("Carmela", 1)
gatuna2 = Hediondos("Lucinda", 1)
perruno1 = Hediondos("Rex", 12)
print(perruno1)

# Los más importantes:

# __main__ : Definido antes.
# __str__ : da la información de la clase de la instancia.
# Información: https://rszalski.github.io/magicmethods/

# *************************************************************************************************************************************

# D E S T R U C T O R :

# Es un metodo mágico o especial que se llama cuando un obeto se destruye o se elimina. Se define como " __del__":


# class MiClase:
#    def __init__(self):
#        print("Objeto creado")

#    def __del__(self):
#        print("Objeto destruido")


# Obj_Ejem = MiClase()

# *************************************************************************************************************************************

# C O M P A R A N D O   O B J E T O S :


class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon

    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon


coords1 = Coordenadas(45, 27)   # Instancia 1
coords2 = Coordenadas(45, 27)   # Instancia 2

# ¿Son las mismas instancias si tienen los mismos valores? NO.
# Imprime False, puesto que el espacio en memoria RAM (física) es distinto.
print(coords1 == coords2)
# Con el signo "==", se está consultando si las Instancias son copia una de la otra.
# Para que sean iguales, se debe implementar un método mágico o especial: "__eq__".
# Aqui devuelve el valor de "True".
print(coords1 == coords2)
# En ese sentido, ambas instancias son iguales, ubicadas en distintas memorias.

# __ne__ : Not Equal.
# Si se consulta por la desingualdad o no igualdad, imprime "False".
print(coords1 != coords2)
print(coords1, coords2)
