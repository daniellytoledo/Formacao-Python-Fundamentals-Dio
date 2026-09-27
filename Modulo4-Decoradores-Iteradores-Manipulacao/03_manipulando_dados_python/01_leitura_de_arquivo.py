"""
Python fornece várias maneiras de ler um arquivo. Podemos usar read(), readline() ou readlines() dependendo de nossas necessidades.
"""

# Ler todo o conteúdo do arquivo de uma ve
file = open("lorem.txt", "r")
print(file.read())
file.close()

"""
Método readline e readlines

O método readline() lê uma linha por vez, enquanto readlines() retorna uma lista onde cada elemento é uma linha do arquivo.
"""

# Ler uma linha por vez, mostrando apenas a primeira linha do texto
file = open("lorem.txt", "r")

print(file.readline())
# Mas se chamarmos de novo, aí ele trás outra linha, e assim por diante
print(file.readline())
# Se colocarmos readline() dentro de um for, ele vai ler a primeira linha e mostrar caracter por caracter
for linha in file.readline():
    print(linha)
file.close()

# Mas se usarmos o readlines() no for, aí sim ele volta mostrando todo o conteúdo
file = open("lorem.txt", "r")

for linha in file.readlines():
    print(linha)

file.close()

# Usar o while para ler linha por linha e quando não houve mais linhas com conteúdo, ou seja, se a linha estiver vazia, ele automáticamente para de ler
file = open("lorem.txt", "r")
while len(linha := file.readline()):
    print(linha)
file.close()