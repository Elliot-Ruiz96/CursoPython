from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from main import Ejemplo

# Windows -> desinger.exe

# Inicializacon de gui
app = QApplication(sys.argv)
# Inicializacion de ventana principal
window = QMainWindow()
# window = Ejemplo()
# Muestra la ventana creada
window.show()
# Ejecucion de gui
sys.exit(app.exec_())
