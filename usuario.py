class Usuarios:
    def __init__(self,nombre,edad,id):
        self.nombre=nombre
        self._edad=edad
        self.__id=id

        @property
        def nombre(self):
            return self.nombre
        
        def edad(self):
            return self._edad
        
        def id():
            return self.__id
        
        @nombre.setter
        def nombre(self,nombre):
            if (len(nombre))<1:
                raise TypeError("Ingrese un nombre valido")
            self.nombre=nombre
            return nombre
        
        def edad(self,valor):
            if not isinstance (valor,str):
                raise TypeError("La edad debe ser numerica")
            if valor<0:
                raise TypeError("La edad debe ser positiva")
            self._edad=valor
            return edad

        def id(self,ide):
            if (len(nombre))<1:
                raise TypeError("La ID no puede ser nada")
            if ide in id:
                raise NameError("ID en uso")
            self.__id=ide
            return ide

    def registrar_usuario(self):
        self.nombre()
        self.edad()
        self.id()

    def mostrarU(self):
        return Usuarios(self)
