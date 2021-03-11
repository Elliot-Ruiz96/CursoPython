from PySide6 import QtWidgets
from estudiante import Estudiante
import sys
import socket
import pickle

host = '3.16.226.150'
port = 9997


class Menu(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)

        nameLabel1 = QtWidgets.QLabel("Nombre:")
        self.nameLine = QtWidgets.QLineEdit()
        nameLabel2 = QtWidgets.QLabel("Correo:")
        self.mailLine = QtWidgets.QLineEdit()
        nameLabel3 = QtWidgets.QLabel("Contraseña:")
        self.passLine = QtWidgets.QLineEdit()

        self.submitButton = QtWidgets.QPushButton("&Buscar y enviar")
        self.submitButton.setToolTip("Cargar archivo .zip")

        self.submitButton.clicked.connect(self.submitAlumno)

        buttonLayout1 = QtWidgets.QVBoxLayout()
        buttonLayout1.addWidget(self.submitButton)

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

    def submitAlumno(self):

        s = socket.socket()
        # Port = 9997 proyecto final, 9998 pruebas
        s.connect((host, port))

        estudiante = Estudiante(self.nameLine.text(), self.mailLine.text(), self.passLine.text())
        estudiante_seriado = pickle.dumps(estudiante)

        s.send(estudiante_seriado)
        res = s.recv(1024)
        print(f'Respuesta: \n\t{res.decode()}')

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                            "Open ZIP file",
                                                            '',
                                                            "Zip file (*.zip);;All Files (*)")
        if not fileName:
            return

        fileName_seriado = pickle.dumps(fileName)

        i = True
        j = 0

        while i:
            chunk = fileName_seriado[j: j + 1024]

            if not chunk:
                i = False
                continue

            s.send(b'INI')
            res = s.recv(1024)
            print(f'Respuesta: \n\t{res.decode()}')

            s.send(chunk)
            res = s.recv(1024)
            print(f'Respuesta: \n\t{res.decode()}')
            j += 1024

        s.send(b'FIN')
        res = s.recv(1024)
        print(f'Respuesta: \n\t{res.decode()}')

        s.close()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Menu = Menu()
    Menu.show()
    sys.exit(app.exec_())
