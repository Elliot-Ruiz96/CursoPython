import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import *
from mongoengine import *

connect('IECA', host='Localhost', port=27017)


class estudiantes(Document):
    Nombre_estudiante = StringField(required=True, max_length=200)
    Correo_estudiantil = StringField(required=True)
    Contrasenia = StringField(required=True)
    Materias = StringField(required=True)


# def escritura(student):
# def lectura():
# def modificacion():


class Menu(QtWidgets.QWidget):

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

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarea 5")
        self.layout = QtWidgets.QVBoxLayout(self)
        # Se usara el mismo objeto para dedicar menos memoria
        self.t1 = QtWidgets.QLabel("TAREA 5", alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.t1)
        self.B1 = QtWidgets.QPushButton("1. Ingresar estudiante")
        self.layout.addWidget(self.B1)
        self.B2 = QtWidgets.QPushButton("2. Modificar estudiantes")
        self.layout.addWidget(self.B2)
        self.B3 = QtWidgets.QPushButton("3. Mostrar Estudiantes")
        self.layout.addWidget(self.B3)
        self.B4 = QtWidgets.QPushButton("4. Salir")
        self.layout.addWidget(self.B4)
        self.B1.clicked.connect(self.escritura)
        self.B2.clicked.connect(self.modificacion)
        self.B3.clicked.connect(self.lectura)
        self.B4.clicked.connect(quit)
        self.layout = QtWidgets.QVBoxLayout(self)

    def escritura(self):
        self.t1 = QtWidgets.QLabel("Ingresa nombre del estudiante: ")
        self.layout.addWidget(self.t1)
        self.e1 = QLineEdit()
        self.layout.addWidget(self.e1)
        self.t1 = QtWidgets.QLabel("Ingresa correo del estudiante: ")
        self.layout.addWidget(self.t1)
        self.e2 = QLineEdit()
        self.layout.addWidget(self.e2)
        self.t1 = QtWidgets.QLabel("Ingresa contrasenia del estudiante: ")
        self.layout.addWidget(self.t1)
        self.e3 = QLineEdit()
        self.layout.addWidget(self.e3)
        self.t1 = QtWidgets.QLabel("Ingresa materias del estudiante: ")
        self.layout.addWidget(self.t1)
        self.e4 = QLineEdit()
        self.layout.addWidget(self.e4)
        comp_nom = self.e1
        comp_cor = self.e2
        comp_con = self.e3
        comp_mat = self.e4
        aceptado = True
        repetido = None
        for datos in estudiantes.objects:
            comp_nom != datos.Nombre_estudiante
            comp_cor != datos.Correo_estudiantil
            comp_con != datos.Contrasenia
            comp_mat != datos.Materias
            if comp_nom and comp_cor and comp_con and comp_mat:
                aceptado = True
                repetido = False
            else:
                print("Estudiante ya ingresado")
                repetido = True
                input("Presione enter para continuar")

        if aceptado:
            datos = estudiantes(
                Nombre_estudiante=comp_nom,
                Correo_estudiantil=comp_cor,
                Contrasenia=comp_con,
                Materias=comp_mat)

            if repetido is True:
                pass
            else:
                datos.save()

    def modificacion(self):
        p = estudiantes.objects(Nombre_estudiante="Cesar")
        estudiantes.objects(Nombre_estudiante=p[0].Nombre_estudiante).update_one(set__Nombre_estudiante="Hola")
        estudiantes.objects(Materias=p[0].Materias).update_one(set__Materias="Adios")
        print(p[0].Contraseña)
        p[0].save()

    def lectura(self):
        i = 1
        for Datos in estudiantes.objects:
            self.t1 = QtWidgets.QLabel(f"Estudiante {i}")
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(estudiantes.Nombre_estudiante.name)
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(Datos.Nombre_estudiante)
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(estudiantes.Correo_estudiantil.name)
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(Datos.Correo_estudiantil)
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(estudiantes.Contrasenia.name)
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(Datos.Contrasenia)
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(estudiantes.Materias.name)
            self.layout.addWidget(self.t1)
            self.t1 = QtWidgets.QLabel(Datos.Materias)
            self.layout.addWidget(self.t1)
            i += 1

        if i == 1:
            self.t1 = QtWidgets.QLabel("Base de datos vacias.")
            self.layout.addWidget(self.t1)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = Menu()
    widget.resize(600, 450)
    widget.show()
    sys.exit(app.exec_())
