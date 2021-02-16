import pickle

file = open('data.dat', 'wb')

animals = ['python', 'monkey', 'camel']

pickle.dump(animals, file, 2)

pass