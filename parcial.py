from usuario import Usuarios
from libros import Libros

def nain():
    print("Bienvenido a la Biblioteca Universitaria")
    opc=int(input("Ingrese 1 para registrar usuario, ingrese 2 para registrar libros: "))

    if (opc==1):
        name=input("Ingrese su nombre: ")
        age=input("Ingrese su edad: ")
        ident=input("Cree su ID: ")

        Usuarios(nombre=name, edad=age, id=ident).registrar_usuario
        print(f"Usuario creado exitosamente, Nombre: ",name,", Edad: ",age,", ID creada: ",ident)

    if (opc==2):
        book=input("Ingrese el nombre del libro: ")
        genrer=int(input("Ingrese el genero (1 para matematicas, 2 para ciencias y 3 para humanas): "))

        if (genrer==1):
            genrer="matematicas"
        if (genrer==2):
            genrer="ciencias"
        if (genrer==3):
            genrer="humanas"

        Libros(titulo=book, categoria=genrer).registrar_libro
        print(f"Libro agregado exitosamente, Titulo: ",book,", Genero: ",genrer)

nain()
