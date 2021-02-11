# Un modulo es un archivo con funciones

def funcion(nombre):
    print('Hello', nombre)

    return({1: 'uno'},[2],(3))

if __name__ == '__main__':
    ret, r2, r3 = funcion('Pedro')

    print(ret, r2, r3)
