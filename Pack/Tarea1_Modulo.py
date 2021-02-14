#import random
#s_user = input()
#s_pc = random.choice(['piedra', 'papel', 'tijera'])
#s_user = 'piedra', s_pc = 'tijera'


def funcion(s_user, s_pc):

    if s_user != s_pc:
        if s_user == 'piedra':
            if s_pc == 'papel':
                print('Perdiste!')
            else:
                print('Ganaste!')
        elif s_user == 'papel':
            if s_pc == 'tijera':
                print('Perdiste!')
            else:
                print('Ganaste!')
        elif s_user == 'tijera':
            if s_pc == 'piedra':
                print('Perdiste!')
            else:
                print('Ganaste!')
        else:
            print('Seleccion no valida!')
    else:
        print('Empate!')


