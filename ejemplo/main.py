# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Ejemplo(QWidget):
    def __init__(self):
        super(Ejemplo, self).__init__()
        self.load_ui()

        #self.pushButton.clicked.connect(slot1)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "ejemplo.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def slot1(self):
        print('Boton presionado!')

    def fun1 (self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    widget = Ejemplo()
    widget.show()
    sys.exit(app.exec_())
