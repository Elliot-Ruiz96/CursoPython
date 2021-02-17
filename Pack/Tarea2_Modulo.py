import re


def validacion(correo, telefono):

    # Variable para validacion de correo
    valida_correo = re.search("@", correo)
    valida_correo_dominio = re.split("@", correo)
    # Variable para validacion de telefono
    valida_telefono = re.findall("\d", telefono)

    if valida_correo:
        print("Yes")
    if re.search("[.]", valida_correo_dominio[1]):
        print("Yes")
    else:
        print(f'Correo {correo} no valido.')

    if len(valida_telefono) == 10:
        print("Yes")
    else:
        print(f'Numero {telefono} no valido.')


if __name__ == '__main__':
    validacion("jj@gmail.com", "4775531264")
