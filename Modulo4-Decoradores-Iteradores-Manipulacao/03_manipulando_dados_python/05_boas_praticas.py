"""
Bloco with

Use o gerenciamento de contexto (context manager) com a declaração 'with'. O gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções.

"""

from pathlib import Path

ROOT_PATH = Path(__file__).parent

# como aprendemos a abrir e fechar arquivo
arquivo = open(ROOT_PATH / "lorem.txt", "r")
arquivo.close()

# com o with podemos automatizar o fechamento do arquivo por questões de segurança e também para liberar recursos
with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
    print("Trabalhando com o arquivo.")

# é recomendado verificar se o arquivo foi aberto corretamente antes de executar operações de leitura ou gravação nele
try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

# certifique-se de usar a codificação correta ao ler ou gravar arquivos de texto. o argumento 'encoding' da função 'open()' permite especificar a codificação.
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
except IOError:
    pass

