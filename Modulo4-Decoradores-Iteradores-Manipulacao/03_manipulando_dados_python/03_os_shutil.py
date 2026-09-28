"""
Python também oferece funções para gerenciar arquivos e diretórios. Podemos criar, renomear e excluir arquivos e diretórios usando os módulos 'os'e 'shutil'.
"""

import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent # vai colocar o caminho do arquivo na variável root_path usando p Path(__file__) | o .parent seleciona quem está acima do arquivo atual, ou seja, a pasta que o arquivo está inserido. então o que vai ficar guardado na variável é caminho da pasta, facilitando para não termos que ficar copiando o caminho manualmente quando quisermos criar um arquivo em determinada pasta ou mudar de diretório algum arquivo. Isso também facilita a padronização do caminho, pois sistemas como Windows e Linux usam barras \/ em diferentes direções 

os.mkdir(ROOT_PATH / "novo_diretorio") # vai criar a pasta novo_diretorio dentro do caminho que foi salvo na variável root_path

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") # alterar o nome do arquivo

os.remove(ROOT_PATH / "alterado.txt") # remover o arquivo

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo_diretorio" / "novo.txt") # move o arquivo para a nova pasta

