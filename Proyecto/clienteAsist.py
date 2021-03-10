from PySide6 import QtWidgets
from PySide2 import QtWidgets
from estudiante import Estudiante
import sys
import socket
import pickle


# Clase padre para el menu
class Menu(QtWidgets.QWidget):
    ModoNavegar, ModoIngresar, ModoEditar = range(3)

    # Funcion para declarar e inicializar los widgets
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)

        # Se realiza la codificacion en lugar del archivo ui

        nameLabel1 = QtWidgets.QLabel("Nombre:")
        self.nameLine = QtWidgets.QLineEdit()

        nameLabel2 = QtWidgets.QLabel("Correo:")
        self.mailLine = QtWidgets.QLineEdit()

        nameLabel3 = QtWidgets.QLabel("Contraseña:")
        self.passLine = QtWidgets.QLineEdit()

        # Botones para funcion de menu
        self.submitButton = QtWidgets.QPushButton("&Confirma")
        # Cambiar para archivo
        self.codeButton = QtWidgets.QPushButton("&Buscar...")
        self.codeButton.setToolTip("Cargar archivo .zip")

        # Definir la conexion a funciones
        self.submitButton.clicked.connect(self.submitAlumno)
        self.codeButton.clicked.connect(self.buscarCodigo)

        # Layout de funciones principales
        buttonLayout1 = QtWidgets.QVBoxLayout()
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.codeButton)
        buttonLayout1.addStretch()

        # Layout principal con coordenadas
        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(nameLabel1, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(nameLabel2, 1, 0)
        mainLayout.addWidget(self.mailLine, 1, 1)
        mainLayout.addWidget(nameLabel3, 2, 0)
        mainLayout.addWidget(self.passLine, 2, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("Proyecto")

    def submitAlumno(self, fileName):
        # Agregar clase estudiante
        s = socket.socket()

# Port = 9997 proyecto final
# Port = 9998 pruebas

        host = '3.16.226.150'
        port = 9998

        s.connect((host, port))

        estudiante = Estudiante(self.nameLine.text(), self.mailLine.text(), self.passLine.text())

        estudiante_seriado = pickle.dumps(estudiante)

        s.send(estudiante_seriado)

        res = s.recv(1024)
        print(f'Respuesta: \n\t{res.decode()}')

        s.close()

    def buscarCodigo(self):
        s = socket.socket()

        host = '3.16.226.150'
        port = 9998

        s.connect((host, port))

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                            "Open ZIP file",
                                                            '',
                                                            "Zip file (*.zip);;All Files (*)")
        if not fileName:
            return

        fileName_seriado = pickle.dumps(fileName)

        s.send(fileName_seriado)

        res = s.recv(1024)
        print(f'Respuesta: \n\t{res.decode()}')

        s.close()
        

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Menu = Menu()
    Menu.show()
    sys.exit(app.exec_())
