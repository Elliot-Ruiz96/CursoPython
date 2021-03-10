import pickle


class Estudiante:

    def __init__(self, nombre, carrera, correo, num_control, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.num_control = num_control
        self.promedio = promedio

    def setnombre(self):
        nombre = input()
        self.nombre = nombre

    def getnombre(self):
        return self.nombre

    def setcarrera(self):
        carrera = input()
        self.carrera = carrera

    def getcarrera(self):
        return self.carrera

    def setcorreo(self):
        correo = input()
        self.correo = correo

    def getcorreo(self):
        return self.correo

    def setnum_control(self):
        num_control = input()
        self.num_control = num_control

    def getnum_control(self):
        return self.num_control

    def setpromedio(self):
        promedio = input()
        self.promedio = promedio

    def getpromedio(self):
        return self.promedio


# e = Estudiante(nombre, carrera, correo, num_control, promedio)
e = Estudiante("Elliot", "MECATRONICA", "elliotruizs@iee.org", "16240056", "82.47")
e1 = Estudiante("DIEGO", "ACTUARIA", "diegovo@iee.org", "16240057", "83.47")
e2 = Estudiante("RENE", "SISTEMAS", "reneva@iee.org", "16240058", "84.47")
e3 = Estudiante("SERGIO", "GESTION", "sergiorv@iee.org", "16240059", "85.47")
e4 = Estudiante("KARLA", "ADMINISTRACION", "karlahe@iee.org", "16240060", "86.47")


def agregar():
    # [PV] Solo se cambia el priemr objeto
    print("Ingresa tu nombre completo: ")
    e.setnombre()
    print("Ingresa tu carrera: ")
    e.setcarrera()
    print("Ingresa tu correo: ")
    e.setcorreo()
    print("Ingresa tu numero de control: ")
    e.setnum_control()
    print("Ingresa tu promedio: ")
    e.setpromedio()


def lectura():
    # [PV] Se puede usar un loop para mostrarlos todos
    print("Nombre:")
    print(e.getnombre())
    print('Carrera:')
    print(e.getcarrera())
    print('Correo:')
    print(e.getcorreo())
    print('Numero de control:')
    print(e.getnum_control())
    print('Promedio:')
    print(e.getpromedio())


def actualizar():
    # [PV] Siempre se edita el primer objeto
    print("Ingresa tu nombre completo: ")
    e.setnombre()
    print("Ingresa tu carrera: ")
    e.setcarrera()
    print("Ingresa tu correo: ")
    e.setcorreo()
    print("Ingresa tu numero de control: ")
    e.setnum_control()
    print("Ingresa tu promedio: ")
    e.setpromedio()


def pickle1():
    ej_dict = {1: e.nombre, 2: e.carrera, 3: e.correo, 4: e.num_control, 5: e.promedio}
    ej_dict1 = {1: e1.nombre, 2: e1.carrera, 3: e1.correo, 4: e1.num_control, 5: e1.promedio}
    ej_dict2 = {1: e2.nombre, 2: e2.carrera, 3: e2.correo, 4: e2.num_control, 5: e2.promedio}
    ej_dict3 = {1: e3.nombre, 2: e3.carrera, 3: e3.correo, 4: e3.num_control, 5: e3.promedio}
    ej_dict4 = {1: e4.nombre, 2: e4.carrera, 3: e4.correo, 4: e4.num_control, 5: e4.promedio}
    pickle_out = open("dict.db", "wb")
    pickle.dump(ej_dict, pickle_out)
    pickle.dump(ej_dict1, pickle_out)
    pickle.dump(ej_dict2, pickle_out)
    pickle.dump(ej_dict3, pickle_out)
    pickle.dump(ej_dict4, pickle_out)
    pickle_out.close()
    pickle_in = open("dict.db", "rb")
    example_dict = pickle.load(pickle_in)
    print(example_dict)
    print(example_dict[2])
