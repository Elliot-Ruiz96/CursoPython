from Pack.StudentIO import agregar
from Pack.StudentIO import lectura
from Pack.StudentIO import actualizar


def menu():
    choice = input()
    if choice == '1':
        agregar()
    elif choice == '2':
        lectura()
    elif choice == '3':
        actualizar()
    else:
        print("Eleccion no valida. ")


print("Bienvenido a la tarea 3.")
print("1. Agregar nuevo alumno.")
print("2. Lectura de alumno.")
print("3. Actualizar alumno.")
print("4. Salir del programa")
print("Ingrese su eleccion: ")
menu()
