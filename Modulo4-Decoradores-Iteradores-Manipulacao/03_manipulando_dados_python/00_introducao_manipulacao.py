"""
Por que precisamos manipular arquivos?

Os arquivos são essenciais para qualquer tipo de programação, pois fornecem um meio de armazenar e recuperar dados. Através da manipulação de arquivos, podemos persistir os dados além da vida útil de um programa específico.

Conceito de arquivo em informática

Um arquivo é um container no computador onde as informações são armazenadas em formato digital. Existem dois tipos de arquivos que podemos manipular em Python: arquivos de texto e arquivos binários.

Por que precisamos manipular arquivos?

Para manipular arquivos em Python, primeiro precisamos abrí-los. Usamos uma função open() para isso. Quando terminamos de trabalhar com o arquivo, usamos a função close() para liberar recursos e capacidade computacional.

Exemplo:

file = open("example.txt", "r")
...fazemos algo com o arquivo
file.close()

Modos de abertura de arquivo

Existem diferentes modos para abrir um arquivo, como somente leitura ('r'), gravação ('w') e anexar ('a'). O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar no mesmo.

Para ler um arquivo:                         file = open("exemplo.txt", "r")
Para escrever em um arquivo:                 file = open("exemplo.txt", "w")
Para anexar conteúdo a um arquivo existente: file = open("exemplo.txt", "a")
"""