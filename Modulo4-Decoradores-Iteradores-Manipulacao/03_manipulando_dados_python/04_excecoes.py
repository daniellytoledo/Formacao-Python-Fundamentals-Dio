"""
Tratar erros é uma parte importante da manipulação de arquivos. Python oferece uma variedade de exceções que nos permitem lidar com erros comuns.

Exceções mais comuns

FileNotFoundError: lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretório especificado.

PermissionError: lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.

IOError: lançada quando ocorre um erro geral de E/S (entrada/saída) ao trabalhador com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.

UnicodeDecodeError: lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.

UnicodeEncodeError: lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo de texto.

IsADirectoryError: lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto.
"""

# tentando abrir um arquivo que não existe
try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)


from pathlib import Path
ROOT_PATH = Path(__file__).parent

# tentando abrir um arquivo que na verdade é um diretório (uma pasta)
try:
    arquivo2 = open(ROOT_PATH / "novo_diretorio")
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")

