continuar = True
contador = 0

while continuar:
    contador +=1
    print(f'{contador}')

    print('¿Deseas continuar?')
    print('s = Si')
    print('Cualquier caracter = Si')
    respuesta = input()

    if respuesta == 's':
        continue
    else:
        continuar = False

for i in range(1 , 10 , 2):

    print(f'Numero: {i + 1}')

# La letra 'f' antes del texto indica que hay una variable dentro del print y se escribe dentro de los parentesis,

    if i == 4:
        break

print('FIN')