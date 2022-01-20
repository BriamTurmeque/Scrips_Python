#declaracion de la clase
from wsgiref.validate import validator


class producto:

    # no creamos las variables aqui, sino que las creamos dentro del constructor

    #creacion de un constructor
    def __init__(self, nombre, apellido, precio):

        self.__nombre = nombre   #ese barra barra en la variable me indica que ese
        self.apellido = apellido #atributo es privado 
        self.__precio = precio

    # creacion de los getters y setters

    #para decirle que es un get le tenemos que poner ese arroba
    @property
    def nombre(self):
        return self.__nombre

    #para decirle que es un set le tenemos que poner @atributo.setter
    #el nombre del atributo varia segun el nombre del atributo
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def apellido (self):
        return self.__apellido

    @property
    def precio (self):
        return self.__precio

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor
    

    @precio.setter
    def precio (self, valor):
        self.__precio = valor 

    def __str__(self):
         return 'el nombre es: ' + str(self.__nombre) + ', apellido: ' + str(self.__apellido) + ', precio: ' + str(self.__precio)

p1 = producto("felipe","turmeque",10)

p2 = producto(
    "ronal",
    "roldan",
    10
)

print(p1)
print(p2)
print(p1.nombre)