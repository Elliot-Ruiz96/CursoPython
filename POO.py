class Persona:
    nombre = ''
    correo = ''

    def __init__(self):
        self.edad = 24
        self.nombre = 'Elliot'
        self.correo = 'elliotruizs@ieee.org'

    def saludar(self, nombre):
        print('Hola', nombre)
        print(self.nombre, '\n', self.correo, '\n', self.edad)


# name por que es una variable especifica y main para ejecutarse
if __name__ == '__main__':

    p = Persona()
    p.saludar('ERS')
    print(p)
