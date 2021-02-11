tupla = 'Hola' , 2 , 3.4 , False , [ 1 , 'test' ] , 2 , 2
tupla2 = tuple()

print(f'Tupla: {tupla[0]}')
print(f'Tupla: {tupla[1]}')
print(f'Tupla: {tupla[2]}')
print(f'Tupla: {tupla[3]}')
print(f'Tupla: {tupla[4][1]}')
print(f'Tupla2: {tupla2}')

print(type(tupla2))

conteo = tupla.count(2)
print('Conteo: ' , conteo)
