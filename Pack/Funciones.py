# Un modulo es un archivo con funciones

def funcion( nombre = 'Elliot', apellido = 'Ruiz', lista=['a','b','c','d']):
    print('Hello', nombre, apellido)
    print(f'lista:  {lista}')
    lista[1] = 14

    return lista

if __name__ == '__main__':
    lista = [ 1 , 2 , 3]

    l = funcion(lista=lista.copy())

    print(f'main: {lista}')
    print(l)
