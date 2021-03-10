<<<<<<< HEAD
from PySide6 import QtCore, QtWidgets
=======
# from PySide6 import QtCore, QtWidgets
from PySide2 import QtCore, QtWidgets
>>>>>>> c2b9e651e378cf9e3edeb8068587e5cd18aa8cde
from mongoengine import *
import sys

connect('IECA', host='Localhost', port=27017)


class estudiantes(Document):
    Nombre_estudiante = StringField(required=True, max_length=200)
    Correo_estudiantil = StringField(required=True)
    Contrasenia = StringField(required=True)
    Materias = StringField(required=True)


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


# Clase padre para el menu
class Menu(QtWidgets.QWidget):
    ModoNavegar, ModoIngresar, ModoEditar = range(3)

    # Funcion para declarar e inicializar los widgets
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)

        self.database = estudiantes()
        self.oldName = ''
        self.oldMail = ''
        self.oldPass = ''
        self.oldSubj = ''
        self.ModoActual = self.ModoNavegar

        nameLabel1 = QtWidgets.QLabel("Nombre:")
        self.nameLine = QtWidgets.QLineEdit()
        self.nameLine.setReadOnly(True)

        nameLabel2 = QtWidgets.QLabel("Correo:")
        self.mailLine = QtWidgets.QLineEdit()
        self.mailLine.setReadOnly(True)

        nameLabel3 = QtWidgets.QLabel("Contraseña:")
        self.passLine = QtWidgets.QLineEdit()
        self.passLine.setReadOnly(True)

        nameLabel4 = QtWidgets.QLabel("Materia:")
        self.subjLine = QtWidgets.QLineEdit()
        self.subjLine.setReadOnly(True)

        # Botones para funcion de menu
        self.addButton = QtWidgets.QPushButton("&Ingresa")
        self.editButton = QtWidgets.QPushButton("&Modifica")
        self.editButton.setEnabled(False)
        self.removeButton = QtWidgets.QPushButton("&Elimina")
        self.removeButton.setEnabled(False)
        self.submitButton = QtWidgets.QPushButton("&Confirma")
        self.submitButton.hide()
        self.cancelButton = QtWidgets.QPushButton("&Cancela")
        self.cancelButton.hide()

        # Botones para mostrar
        self.nextButton = QtWidgets.QPushButton("&Siguiente")
        self.nextButton.setEnabled(False)
        self.previousButton = QtWidgets.QPushButton("&Anterior")
        self.previousButton.setEnabled(False)

        # Definir la conecion a funciones
        self.addButton.clicked.connect(self.addAlumno)
        self.editButton.clicked.connect(self.editAlumno)
        self.removeButton.clicked.connect(self.removeAlumno)
        self.submitButton.clicked.connect(self.submitAlumno)
        self.cancelButton.clicked.connect(self.cancelAlumno)
        self.nextButton.clicked.connect(self.nextAlumno)
        self.previousButton.clicked.connect(self.previousAlumno)

        # Layout de funciones principales
        buttonLayout1 = QtWidgets.QVBoxLayout()
        buttonLayout1.addWidget(self.addButton)
        buttonLayout1.addWidget(self.editButton)
        buttonLayout1.addWidget(self.removeButton)
        buttonLayout1.addWidget(self.cancelButton)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addStretch()

        # Layout de funciones mostrar
        buttonLayout2 = QtWidgets.QHBoxLayout()
        buttonLayout2.addWidget(self.nextButton)
        buttonLayout2.addWidget(self.previousButton)

        # Layout principal con coordenadas
        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(nameLabel1, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(nameLabel2, 1, 0)
        mainLayout.addWidget(self.mailLine, 1, 1)
        mainLayout.addWidget(nameLabel3, 2, 0)
        mainLayout.addWidget(self.passLine, 2, 1)
        mainLayout.addWidget(nameLabel4, 3, 0)
        mainLayout.addWidget(self.subjLine, 3, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)
        mainLayout.addLayout(buttonLayout2, 4, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Tarea 5")

    def addAlumno(self):
        self.oldName = self.nameLine.text()
        self.oldMail = self.mailLine.text()
        self.oldPass = self.passLine.text()
        self.oldSubj = self.subjLine.text()

        self.nameLine.clear()
        self.mailLine.clear()
        self.passLine.clear()
        self.subjLine.clear()

        self.updateGUI(self.ModoIngresar)

    def editAlumno(self):
        self.oldName = self.nameLine.text()
        self.oldMail = self.mailLine.text()
        self.oldPass = self.passLine.text()
        self.oldSubj = self.subjLine.text()

        self.updateGUI(self.ModoEditar)

    def removeAlumno(self):
        nombre = self.nameLine.text()

<<<<<<< HEAD
=======
        # [PV] No se interactua con la BD
>>>>>>> c2b9e651e378cf9e3edeb8068587e5cd18aa8cde
        if nombre in self.database:
            boton = QtWidgets.QMessageBox.question(self, "Confirmar", "Estas seguro de quitar a \"%s\"?" % nombre,
                                                   QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if boton == QtWidgets.QMessageBox.Yes:
                self.previous()
                del self.database[nombre]

                QtWidgets.QMessageBox.information(self, "Operacion exitosa", "\"%s\" ha sido eliminado" % nombre)

        self.updateGUI(self.ModoNavegar)

    def submitAlumno(self):
        nombre = self.nameLine.text()
        correo = self.mailLine.text()
        contra = self.passLine.text()
        materi = self.subjLine.text()

        if nombre == "" or correo == "" or contra == "" or materi == "":
            QtWidgets.QMessageBox.information(self, "Campo Vacio", "Por favor ingrese todos lo campos.")
            return

        if self.ModoActual == self.ModoIngresar:
            if nombre not in self.database:
                estudiantes(
                    Nombre_estudiante=nombre,
                    Correo_estudiantil=correo,
                    Contrasenia=contra,
                    Materias=materi)
                QtWidgets.QMessageBox.information(self, "Operacion exitosa", "\%s\" ha sido añadido." % nombre)
<<<<<<< HEAD
=======

                # [PV] No se guarda a la BD
>>>>>>> c2b9e651e378cf9e3edeb8068587e5cd18aa8cde
            else:
                QtWidgets.QMessageBox.information(self, "Operacion fallida", "\%s\" ya ha sido añadido antes." % nombre)
            return

        elif self.ModoActual == self.ModoEditar:
            if self.oldName != nombre:
                if nombre not in self.database:
                    QtWidgets.QMessageBox.information(self, "Operacion exitosa", "\"%s\" ha sido añadido."
                                                      % self.oldName)
<<<<<<< HEAD
=======
                    # [PV] No se interactua con la BD
>>>>>>> c2b9e651e378cf9e3edeb8068587e5cd18aa8cde
                    del self.database[self.oldName]
                    self.database[nombre] = correo
                    self.database[nombre] = contra
                    self.database[nombre] = materi
                else:
                    QtWidgets.QMessageBox.information(self, "Operacion fallida", "\%s\" ya ha sido añadido antes."
                                                      % nombre)
                    return
            elif self.oldMail != correo:
                QtWidgets.QMessageBox.information(self, "Operacion exitosa", "\"%s\" ha sido añadido." % nombre)
                self.database[nombre] = correo
                self.database[nombre] = contra
                self.database[nombre] = materi
            elif self.oldPass != contra:
                QtWidgets.QMessageBox.information(self, "Operacion exitosa", "\"%s\" ha sido añadido." % nombre)
                self.database[nombre] = correo
                self.database[nombre] = contra
                self.database[nombre] = materi
            elif self.oldSubj != materi:
                QtWidgets.QMessageBox.information(self, "Operacion exitosa", "\"%s\" ha sido añadido." % nombre)
                self.database[nombre] = correo
                self.database[nombre] = contra
                self.database[nombre] = materi

        self.updateGUI(self.ModoNavegar)

    def cancelAlumno(self):
        self.nameLine.setText(self.oldName)
        self.mailLine.setText(self.oldMail)
        self.passLine.setText(self.oldPass)
        self.subjLine.setText(self.oldSubj)
        self.updateGUI(self.ModoNavegar)

    def nextAlumno(self):
        nombre = self.nameLine.text()
        it = iter(self.database)

        try:
            while True:
                this_name, _ = it.next()

                if this_name == nombre:
                    next_nombre, next_correo, next_contra, next_materi = it.next()
                    break
        except StopIteration:
            next_nombre, next_correo, next_contra, next_materi = iter(self.database).next()

        self.nameLine.setText(next_nombre)
        self.mailLine.setText(next_correo)
        self.passLine.setText(next_contra)
        self.subjLine.setText(next_materi)

    def previousAlumno(self):
        nombre = self.nameLine.text()

        prev_nombre = prev_correo = prev_contra = prev_materi = None
        for this_name, this_correo, this_contra, this_materi in self.database:
            if this_name == nombre:
                break

            prev_nombre = this_name
            prev_correo = this_correo
            prev_contra = this_contra
            prev_materi = this_materi
        else:
            self.nameLine.clear()
            self.mailLine.clear()
            self.passLine.clear()
            self.subjLine.clear()
            return

        if prev_nombre is None:
            for prev_nombre, prev_correo, prev_contra, prev_materi in self.database:
                pass

        self.nameLine.setText(prev_nombre)
        self.mailLine.setText(prev_correo)
        self.passLine.setText(prev_contra)
        self.subjLine.setText(prev_materi)

    def updateGUI(self, modo):
        self.ModoActual = modo

        if self.ModoActual in (self.ModoIngresar, self.ModoEditar):
            self.nameLine.setReadOnly(False)
            self.nameLine.setFocus(QtCore.Qt.OtherFocusReason)
            self.mailLine.setReadOnly(False)
            self.passLine.setReadOnly(False)
            self.subjLine.setReadOnly(False)

            self.addButton.setEnabled(False)
            self.editButton.setEnabled(False)
            self.removeButton.setEnabled(False)

            self.nextButton.setEnabled(False)
            self.previousButton.setEnabled(False)

            self.submitButton.show()
            self.cancelButton.show()

        elif self.ModoActual == self.ModoNavegar:
            if not self.database:
                self.nameLine.clear()
                self.mailLine.clear()
                self.passLine.clear()
                self.subjLine.clear()

            self.nameLine.setReadOnly(True)
            self.mailLine.setReadOnly(True)
            self.passLine.setReadOnly(True)
            self.subjLine.setReadOnly(True)
            self.addButton.setEnabled(True)

            number = len(self.database)
            self.editButton.setEnabled(number >= 1)
            self.removeButton.setEnabled(number >= 1)
<<<<<<< HEAD
            self.findButton.setEnabled(number > 2)
=======
            # [PV] El boton findButton no existe en otro lugar del programa
            # self.findButton.setEnabled(number > 2)
>>>>>>> c2b9e651e378cf9e3edeb8068587e5cd18aa8cde
            self.nextButton.setEnabled(number > 1)
            self.previousButton.setEnabled(number > 1)

            self.submitButton.hide()
            self.cancelButton.hide()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Menu = Menu()
    Menu.show()
    sys.exit(app.exec_())
