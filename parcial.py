from usuario import Usuarios
from libros import Libros

def nain():
    print("Bienvenido a la Biblioteca Universitaria")
    opc=input("Ingrese 1 para registrar usuario, ingrese 2 para registrar libros: ")

    if (opc==1):
        name=input(print("Ingrese su nombre: "))
        age=input(print("Ingrese su edad: "))
        ident=input(print("Cree su ID: "))

        Usuarios(nombre=name, edad=age, id=ident).registrar_usuario
        Usuarios().mostrarU()

    if (opc==2):
        book=input(print("Ingrese el nombre del libro: "))
        genrer=input(print("Ingrese el genero (1 para matematicas, 2 para ciencias y 3 para humanas): "))

        if (genrer != 1 or genrer != 2 or genrer != 3):
            raise TypeError("Valor no valido")
        Libros(titulo=book, categoria=genrer).registrar_libro
        Libros().mostrarL()

nain()