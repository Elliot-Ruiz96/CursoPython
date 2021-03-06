from mongoengine import *

connect('IECA', host='Localhost', port=27017)
# Pagina mas especifica de mongo engine https://www.tutorialspoint.com/mongoengine/mongoengine_atomic_updates.htm


class estudiantes(Document):
    Nombre_estudiante = StringField(required=True, max_length=200)
    Correo_estudiantil = StringField(required=True)
    Contrasenia = StringField(required=True)
    Materias = StringField(required=True)

# class estudiantesCopia(Document):
#     Nombre_estudiante = StringField(required=True,max_length=200)
#     Correo_estudiantil = StringField(required=True)
#     Contraseña = StringField(required=True)
#     Materias = StringField(required=True)


class Estudiantes:
    nombre = ""
    correo = ""
    contrasenia = ""
    materias = ""

    def __init__(self, nombre, correo, contrasenia, materias):
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia
        self.materias = materias

# def base_Datos:


def escritura(student):
    aceptado = True
    repetido = None
    for datos in estudiantes.objects:
        comp_nom = student.nombre != datos.Nombre_estudiante
        comp_cor = student.correo != datos.Correo_estudiantil
        comp_con = student.contrasenia != datos.Contrasenia
        comp_mat = student.materias != datos.Materias
        if comp_nom and comp_cor and comp_con and comp_mat:
            aceptado = True
            repetido = False
        else:
            print("Estudiante ya ingresado")
            repetido = True
            input("Presione enter para continuar")

    if aceptado:
        datos = estudiantes(
            Nombre_estudiante=student.nombre,
            Correo_estudiantil=student.correo,
            Contrasenia=student.contrasenia,
            Materias=student.materias)

        if repetido is True:
            pass
        else:
            datos.save()


def lectura():
    i = 1
    for Datos in estudiantes.objects:
        print(f"\t****Estudiante{i}****")
        print(f"\t{estudiantes.Nombre_estudiante.name}:{Datos.Nombre_estudiante}")
        print(f"\t{estudiantes.Correo_estudiantil.name}:{Datos.Correo_estudiantil}")
        print(f"\t{estudiantes.Contrasenia.name}:{Datos.Contrasenia}")
        print(f"\t{estudiantes.Materias.name}:{Datos.Materias}")
        print("")
        i += 1

    if i == 1:
        print("Base de datos esta vacia")


def eliminacion():
    estudiantes.objects.delete()
    print("La base de datos fue vaciada")
    print("")


def modificacion():

    # User =  input("Ingresa nombre de usuario a modificar: ")
    # User_nuev = input("Ingresa el nuevo nombre el usuario");
    # estudiantes.objects(Nombre_estudiante = User).update_one(set__Nombre_estudiante = User_nuev)
    # estudiantes.objects(Nombre_estudiante="Cesar").delete()
    # Nombre = input("Nuevo nombre usuario: ")
    # Correo = input("Nuevo Correo: ")
    # Contra = input("Nueva contraseña: ")
    # Materias = input("Nuevas Materias: ")
    # Modify= estudiantes.objects(Nombre_estudiante=Nombre,
    #         Correo_estudiantil=Correo,
    #         Contraseña=Contra,
    #         Materias=Materias)
    # Eliminar[0].delete()

    # Eliminar[0].deleted()
    p = estudiantes.objects(Nombre_estudiante="Cesar")
    estudiantes.objects(Nombre_estudiante=p[0].Nombre_estudiante).update_one(set__Nombre_estudiante="Hola")
    estudiantes.objects(Materias=p[0].Materias).update_one(set__Materias="Adios")
    print(p[0].Contraseña)
    p[0].save()


def menu():
    ciclo = True

    while ciclo:
        print("")
        print("*****Base de datos IECA*****")
        print("")
        print("Ingresar estudiante  ---> 1")
        print("Modificar estudiante ---> 2")
        print("Mostrar estudiantes  ---> 3")
        print("Eliminar estudiantes ---> 4")
        print("Salir                ---> 5")
        opcion = input("Seleciona un opcion  ---> ")

        if opcion == "1":
            print("")
            nombre = input("Ingresa nombre del estudiante: ")
            correo = input("Ingresa correo del estudiante: ")
            contrasenia = input("Ingresa contrasenia del estudiante: ")
            materias = input("Ingresa materias del estudiante: ")
            escritura(Estudiantes(nombre, correo, contrasenia, materias))

        if opcion == "2":
            modificacion()

        if opcion == "3":
            lectura()
            input("Presiona enter para continuar")

        if opcion == "4":
            eliminacion()
            input("Presiona enter para continuar")
            
        if opcion == "5":
            ciclo = False


if __name__ == '__main__':
    menu()
