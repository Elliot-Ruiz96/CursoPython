import pickle

s = 'Hola mundo'

print(s)
print(type(s))

se = s.encode()

print(se)
print(type(se))

sp = pickle.dumps(s)

print(sp)
print(type(sp))

ss2 = pickle.loads(se)

print(ss2)
print(type(ss2))

# No imprime debido a que encuenra una h primero en lugar de la direccion \x80

