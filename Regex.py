import re

texto = 'Buenas tardes a todos y todas'

patron = 'B.*t.*a'
patron2 = 'd[aeo]s'

coincidencia = re.match(patron, texto)

coincidencia2 = re.search(patron, texto)

encontrar = re.findall(patron2, texto)

pass
