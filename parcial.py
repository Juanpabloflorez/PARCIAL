from user import Usuarios
from libros import Libros
import firebase_admin
from firebase_admin import db,credentials

cred=credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://trabajo-opcional-puntos-extra-default-rtdb.firebaseio.com/"})

ref = db.reference("/")

def registrarUsuario():
        name=input("Ingrese su nombre: ")
        age=input("Ingrese su edad: ")
        ident=input("Cree su ID: ")

        Usuarios(nombre=name, edad=age, id=ident).registrar_usuario
        ref.child("Usuarios").child(ident).set({"Nombre": name,"Edad": age})

        print(f"Usuario creado exitosamente, Nombre: ",name,", Edad: ",age,", ID creada: ",ident)

   
def registrarLibro():
        book=input("Ingrese el nombre del libro: ")
        genero=int(input("Ingrese el genero (1 para matematicas, 2 para ciencias y 3 para humanas): "))
        bookID=input("Ingrese el codigo del libro: ")

        while genero != 1 and genero != 2 and genero != 3:
             genero = input("Asignacion de genero no valido, ingrese un valor valido del 1 al 3: ")

        if (genero==1):
            genero="matematicas"
        if (genero==2):
            genero="ciencias"
        if (genero==3):
            genero="humanas"
          
        Libros(titulo=book, categoria=genero).registrar_libro
        ref.child("Libros").child(bookID).set({"Nombre": book,"Categoria":genero})

        print(f"Libro agregado exitosamente, Titulo: ",book,", Categoria: ",genero)


def main():
    registrarLibro()

if __name__ == "__main__":
    main()
