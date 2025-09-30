class Libros:
    def __init__(self,titulo,categoria):
         self.titulo=titulo
         self.categoria=categoria

    @property
    def titulo(self):
        return self.titulo

    @titulo.setter
    def titulo(self,titulo):
        if (len(titulo))<1:
            raise TypeError("Ingrese un nombre valido")

    def categoria(self,categoria):
        if categoria != 1 or categoria != 2 or categoria != 3:
            raise TypeError("La categoria no existe")
        self.categoria=categoria

    def registrar_libro(self):
        self.titulo()
        self.categoria()

    def mostrarL(self):
        return Libros(self)
        
