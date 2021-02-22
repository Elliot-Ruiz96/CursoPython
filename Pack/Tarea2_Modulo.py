import re


def validacion(correo, telefono, curp, rfc):

    # Variable para validacion de correo
    # [PV] # La validacion es muy debil, ingresar solo @. lo marca como valida
    # patron sencillo '[a-z.]+@([a-z.]+){1,2}[a-z]{2-3}'
    valida_correo = re.search("@", correo)          # Busca el arroba
    valida_correo_dominio = re.split("@", correo)   # Divide en dos grupos el correo

    # Variable para validacion de telefono
    # [PV] Busca que haya 10 numeros pero no valida la forma
    # [PV] ej. '\([0-9]{3}\) [0-9]{3}-[0-9]{4}'
    valida_telefono = re.findall("\d", telefono)    # Verifica que sean solo numeros

    # Variable para validacion de curp
    # [PV] Si se escriben puros numeros se toma com valido
    # ej. valido [A-Z]{4}[0-9]{6}[H|M][A-Z]{5}[A-Z0-9]{2}
    valida_curp = re.search("\S", curp)             # Busca que no haya espacios

    # Variable para validacion de rfc
    # [PV] Si se escriben puros numeros se toma com valido
    # ej. valido [A-Z]{4}[0-9]{6}[A-Z0-9]{3}
    valida_rfc = re.search("\S", rfc)  # Busca que no haya espacios

    if valida_correo:
        if re.search("[.]", valida_correo_dominio[1]):      # Busca el punto en el dominio
            print(f'Correo {correo} valido.')
        else:
            print(f'Correo {correo} no valido.')
    else:
        print(f'Correo {correo} no valido.')

    if len(valida_telefono) == 10:                          # Valida que sean 10 numeros
        print(f'Numero {telefono} valido.')
    else:
        print(f'Numero {telefono} no valido.')

    if len(curp) == 18:                                     # Valida que sean 18 caracteres
        if valida_curp:
            print(f'CURP {curp} valida.')
        else:
            print(f'CURP {curp} no valida.')
    else:
        print(f'CURP {curp} no valida.')

    if len(rfc) == 13:                                     # Valida que sean 18 caracteres
        if valida_rfc:
            print(f'RFC {rfc} valida.')
        else:
            print(f'CURP {curp} no valida.')
    else:
        print(f'RFC {rfc} no valida.')

# elliotruizs@ieee.org
# 4775531264
# RUSE960823HGTZNL03
# RUSE9608231H0

# Para validar de una manera mas precisa el rfc y el curp
# se debe validar los diferentes grupos de datos para su construccion
