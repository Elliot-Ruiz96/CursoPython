import sys
# Importando la clase apropiada
from PySide6.QtWidgets import QApplication, QLabel

# Crear instancia QApp
app = QApplication(sys.argv)
# Es posible pasar cualquier argumento a QApp Obj
label = QLabel("Hello World")
label.show()
app.exec_()