# https://docs.python.org/pt-br/3.14/library/datetime.html

from datetime import date, datetime, timedelta

data = date(2023, 7, 19)
print(data) # 2023-07-19

# ---

print(date.today())

data_hora = datetime(1991, 11, 26, 8)
print("Nascimento:", data_hora)

# ---

tipo_carro = 'P'

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.utcnow()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(weeks=tempo_grande)
    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")

# ---

print(date.today() - timedelta(days=1)) # o dia de hoje menos um dia

# resultado = determinada data e hora subtraindo 2 horas 
resultado = datetime(2026, 08, 28, 17, 52, 45) - timedelta(hours=2)
# print só na hora do resultado usando .time()
print(resultado.time())

