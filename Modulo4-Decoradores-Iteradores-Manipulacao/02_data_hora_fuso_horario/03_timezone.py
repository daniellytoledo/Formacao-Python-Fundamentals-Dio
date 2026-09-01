"""
Quando trabalhamos com data e hora, lidar com fusos horários é uma necessidade comum. Python facilita isso através do módulo 'pytz'.
"""

import datetime
import pytz

# Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)

"""
O Python permite fazer isso com o módulo datetime padrão, embora seja um pouco mais complexo do que usando bibliotecas como 'pytz'.
"""

# Criando datetime com timezone SEM o pytz
data = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
print(data)

# Convertendo para outro timezone
data_utc = data.astimezone(datetime.timezone.utc)
print(data_utc)

