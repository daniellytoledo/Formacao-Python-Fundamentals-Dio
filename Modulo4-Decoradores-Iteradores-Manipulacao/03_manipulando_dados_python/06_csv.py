"""
CSV: um formato de arquivo amplamente utilizado para armazenar dados tabulares. CSV é a sigla para 'Comma Separated Values'.

Python fornece um módulo chamado 'csv' para lidar facilmnte com arquivos CSV. Da mesma forma podemos utiliar o módulo 'csv' para escrever em arquivos CSV.

Práticas recomendadas:
    - Usar csv.reader e csv.writer para manipular arquivos csv
    - Fazer o tratamento correto das exceções
    - Ao gravar arquivos CSV definir o argumento newline= no método 'open'
"""

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# criar um arquivo csv
try:
    with open(ROOT_PATH / "usuarios.csv", "w",  newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f'Erro ao criar o arquivo: {exc}')

# ler o arquivo csv
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f'Erro ao ler o arquivo: {exc}')


# deixando o código mais legível ao selecionar as colunas do arquivo
COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row[COLUNA_ID], row[COLUNA_NOME])
except IOError as exc:
    print(f'Erro ao ler o arquivo: {exc}')

# ignorando o cabeçalho com o idx == 0, e formatando o print
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f'ID: {row[COLUNA_ID]}')
            print(f'NOME: {row[COLUNA_NOME]}')
except IOError as exc:
    print(f'Erro ao ler o arquivo: {exc}')

# ou 
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f'ID: {row['id']}')
            print(f'NOME: {row['nome']}')
except IOError as exc:
    print(f'Erro ao ler o arquivo: {exc}')

    