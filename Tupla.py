#En las tuplas no puede cambiar ni un solo valor despues de declararlas al principio
#Si se usa tupla[-1] (un negativo en el indice) busca de fin a inicio
#Los indices empiezan desde 0
# https://recursospython.com/guias-y-manuales/listas-y-tuplas/

tupla = 'Hola' , 2 , 3.4 , False , [ 1 , 'test' ] , 2 , 2
tupla2 = tuple()

print(f'Tupla: {tupla[0]}')
print(f'Tupla: {tupla[1]}')
print(f'Tupla: {tupla[2]}')
print(f'Tupla: {tupla[3]}')
print(f'Tupla: {tupla[4][1]}')
print(f'Tupla(-1): {tupla[-1]}')
print(f'Tupla2: {tupla2}')

print(type(tupla2))

conteo = tupla.count(2)
print('Conteo: ' , conteo)
