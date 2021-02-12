import re

def suma (a,b):
    patron = '[0-9]*$'

    ra = re.match(patron,str(a))
    rb = re.match(patron, str(b))

    if ra and rb:
        return int(a)+int(b)
