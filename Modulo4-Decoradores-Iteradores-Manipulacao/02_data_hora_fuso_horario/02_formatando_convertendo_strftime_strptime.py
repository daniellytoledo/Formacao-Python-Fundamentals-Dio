"""
Python também permite converter e formatar datas e horas. Para isso, usamos os métodos 'strftime' (string format time) e 'strptime' (string parse time).
"""

import datetime

d = datetime.datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M")) # vai mostrar a data e hora atual no formato dia/mês/ano hora:minutos

# Convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)

