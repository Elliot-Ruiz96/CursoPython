class Division:
    divisor = 0
    dividendo = 0
    resultado = 0
    residuo = 0

    def __init__(self, dividendo, divisor):
        self.divisor = divisor
        self.dividendo = dividendo

    def dividir(self):
        pass


class Divisonentera(Division):
    def __init__(self, dividendo, divisor):
        super().__init__(dividendo, divisor)

    def dividir(self):

        return self.dividendo // self.divisor, self.dividendo % self.divisor


class Divisondecimal(Division):
    def __init__(self, dividendo, divisor):
        super().__init__(dividendo, divisor)

    def dividir(self):
        return self.dividendo / self.divisor


if __name__ == '__main__':
    de = Divisonentera(15, 3)
    res = de.dividir()
    print(res)

    dd = Divisondecimal(16, 3)
    res2 = dd.dividir()
    print(res2)
