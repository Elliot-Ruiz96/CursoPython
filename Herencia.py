class Vehiculo:

    __llantas = 4
    __personas = 2
    __lucesencendidas = False

    def acelera(self):
        pass

    def enciendeluces(self):
        self.__lucesencendidas = True

    def apagarluces(self):
        self.__lucesencendidas = False

    def cuantasllantas(self):
        pass


class Motocicleta(Vehiculo):

    def __init__(self):
        self.enciendeluces()
        print(f'Luces encendidas: {self.lucesencendidas()}')
        pass


if __name__ == '__main__':

    m = Motocicleta()
    print(m)
