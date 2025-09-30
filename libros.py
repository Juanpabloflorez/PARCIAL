class Libros:
    def __init__(self,titulo,categoria):
         self.titulo=titulo
         self.categoria=categoria

    @property
    def titulo(self):
        return self.titulo

    @titulo.setter
    def titulo(self,texto):
        if (len(texto))<1:
            raise TypeError("Ingrese un nombre valido")
        self.titulo=texto

    def categoria(self,category):
        if category != 1 or category != 2 or category != 3:
            raise TypeError("La categoria no existe")
        self.categoria=category

    def registrar_libro(self):
        self.titulo()
        self.categoria()

    def mostrarL(self):
        return Libros(self)
        