f = open("./DarthPlagueis.txt", 'w+')   # f: <_io.TextIOWrapper name='./DarthPlagueis.txt' mode='a+' encoding='cp1252'>

g = open("./Pruebas.txt", 'w+')

ret = f.read()
readable = f.readable()
writable = f.writable()

ret2 = g.write('Hola mundo\n')
g.seek(0)

print(readable)
print(writable)

pass
