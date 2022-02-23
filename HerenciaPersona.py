from os import system

# tengo que implementar algo similar a la funcion amiga para 
# poder guardar los datos algo asi como hacer cin

class Persona:

    # no estoy seguro pero creo que no se pueden poner los dos constructores, el vacio y el con datos
    # asi que solo voy a usar el constructor con parametros 

    # creacion del constructor vacio, no es necesario declarar las variables con anterioridad
    # es necesario colacar el barra barra para indicar que esa variable es privada
    # def __init__(self):
    #     self.__nombre = ""
    #     self.__apellido = ""
    #     self.__documento = ""
    #     self.__tipo_identificacion = 0
    
    def __init__(self, _nombre, _apellido, _tipo_identificacion, _documento):
        self.__nombre = _nombre
        self.__apellido = _apellido
        self.__tipo_identificacion = _tipo_identificacion
        self.__documento = str(_documento)
    

    # esta vendria a ser la declaracion de los getter y setter, solo que en python no se le llaman asi
    # pero complen la misma funcion
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def tipo_identificacion(self):
        return self.__tipo_identificacion
    
    @property
    def documento(self):
        return self.__documento

    @nombre.setter
    def nombre(self, newValor):
        self.__nombre = str(newValor)
    
    @apellido.setter
    def apellido ( self, newValor):
        self.__apellido = newValor
    
    @tipo_identificacion.setter
    def tipo_identificacion(self, newValor):
        self.__tipo_identificacion = newValor
    
    @documento.setter
    def documento(self, newValor):
        self.__documento = newValor

    def __str__(self):
        return (f"- Nombre:               {self.__nombre} \n- Apellido:             {self.__apellido}\n- Documento:            {self.__documento}")
# creamos la clase Cliente que va a heredar de la clase padre "persona"
# cuando creamos el __init__ ponemos todas las variables que vayamos a inicializar
# luego ponemos super() o nameClassFather y esto me inicializara la clase padre, solo falta añadirle los nuevos atributos
class Cliente (Persona):
    def __init__(self, _nombre, _apellido, _tipo_identificacion, _documento, _tipo_suscripcion, _descuento):
        super().__init__(_nombre, _apellido, _tipo_identificacion, _documento)
        self.__tipo_suscripcion = _tipo_suscripcion
        self.__descuento = _descuento

    @property
    def tipo_suscripcion(self):
        return self.__tipo_suscripcion

    @property
    def descuento(self):
        return self.__descuento
    
    @tipo_suscripcion.setter
    def tipo_suscripcion(self, newValor):
        self.__tipo_suscripcion = newValor

    @descuento.setter
    def descuento( self, newValor):
        self.__descuento = newValor

    def __str__(self) -> str:
        return (super().__str__() + f"\n- Tipo de suscripcion:  {self.__tipo_suscripcion}\n- Descuento:            {self.__descuento}\n" )

def titulo():
    print ("########################################")
    print ("###  SISTEMA DE GESTION DE EMPRESAS  ###")
    print ("########################################\n")

def menu(p,c):
    a = "0"
    while a != "3":
        system("cls")
        titulo()
        print ("\n1. Clientes\n2. Empleados\n3. Salir")
        a = str(input("\nDigite una opcion: "))  
        if a == "1":
            menuClientes(c)
        elif a == "2":
            print ("\n>>>Proximamente estara disponible la funcionalidad ;)\n")
            system("pause")

        
        

def menuClientes(c1):
    aux = ""
    while aux != "5":
        system("cls")
        titulo()
        print ("\nGestion de clientes\n\nMenu:\n\n1. Crear clientes\n2. Modificar clientes\n3. Ver clientes\n4. Generar facturas\n5. regresar \n\n")
        aux = str ( input ("Digite una opcion: "))
        print ("")
        if aux == "3":
            system("cls")
            print (c1)
            system("pause")
    

p1 = Persona("Felipe","Roldan",0,"1118528444")
c1 = Cliente ("Carlos" , "turmeque" , 2 , "1118554623" , "2" , 20)

menu(p1,c1)


        
        