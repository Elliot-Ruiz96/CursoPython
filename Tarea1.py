from Pack.Tarea1_Modulo import funcion
import random


def main():
    funcion(s_user, s_pc)


if __name__ == '__main__':
    print('Bienvenido al juego de piedra, papel o tijera')
    print('Escribe tu eleccion: ')
    s_user = input()
    s_pc = random.choice(['piedra', 'papel', 'tijera'])
    print('Eleccion de usuario: ',s_user)
    print('Eleccion de PC: ', s_pc)
    main()

