#import random
#s_pc = random.choice(['piedra', 'papel', 'tijera'])


def funcion(s_user = 'piedra', s_pc = 'tijera'):

    if s_user != s_pc:
        if s_user == 'piedra':
            if s_pc == 'papel':
                resultado = 'Perdiste!'
                print(resultado)
                # print('Perdiste!')
            else:
                resultado = 'Ganaste!'
                print(resultado)
                # print('Ganaste!')
        elif s_user == 'papel':
            if s_pc == 'tijera':
                resultado = 'Perdiste!'
                print(resultado)
                # print('Perdiste!')
            else:
                resultado = 'Ganaste!'
                print(resultado)
                # print('Ganaste!')
        elif s_user == 'tijera':
            if s_pc == 'piedra':
                resultado = 'Perdiste!'
                print(resultado)
                # print('Perdiste!')
            else:
                resultado = 'Ganaste!'
                print(resultado)
                # print('Ganaste!')
        else:
            resultado = 'Seleccion no valida!'
            print(resultado)
            # print('Seleccion no valida!')
    else:
        resultado = 'Empataste!'
        print(resultado)
        # print('Empate!')

    return resultado


if __name__ == '__main__':
    print('Tarea1')