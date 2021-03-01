from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from main import Ui_Form

# Windows -> desinger.exe

# Inicializacon de gui
app = QApplication(sys.argv)
# Inicializacion de ventana principal
# window = QMainWindow()
window = Ui_Form()
# Muestra la ventana creada
window.show()
# Ejecucion de gui
sys.exit(app.exec_())
