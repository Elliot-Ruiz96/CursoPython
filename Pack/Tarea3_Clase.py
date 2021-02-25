class Estudiante:

    def __init__(self):
        self.nombre = "Elliot Ruiz"
        self.carrera = "Mecatronica"
        self.correo = "elliotruizs@iee.org"
        self.num_control = "16240056"
        self.promedio = "82.47"

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


e = Estudiante()
