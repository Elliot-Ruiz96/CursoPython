#Modulo para seleccion aleatoria de PC
#import numpy as np

print('Bienvenido al juego de piedra, papel o tijera')
print('Escribe tu eleccion: ')

#Seleccion de opciones usuario y PC
seleccion_usuario = input()
print('Escribe tu eleccion2: ')
seleccion_pc = input()
#seleccion_pc = np.random.choice(['piedra','papel','tijera'])

if seleccion_usuario != seleccion_pc:
    if seleccion_usuario == 'piedra':
        if seleccion_pc == 'papel':
            print('Perdiste!')
        else:
            print('Ganaste!')
    elif seleccion_usuario == 'papel':
        if seleccion_pc == 'tijera':
            print('Perdiste!')
        else:
            print('Ganaste!')
    elif seleccion_usuario == 'tijera':
        if seleccion_pc == 'piedra':
            print('Perdiste!')
        else:
            print('Ganaste!')
    else:
        print('Seleccion no valida!')
else:
    print('Empate!')
