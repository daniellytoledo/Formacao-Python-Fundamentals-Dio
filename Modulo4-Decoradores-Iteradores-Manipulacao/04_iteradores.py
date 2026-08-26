"""
Introdução

Em Python, um iterador é um objeto que contém um número contável de valores que podem ser iterados, o que significa que você pode percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais "__iter__()" e "__next__()"

Usos:

1. Ler arquivos grandes
    - Economizar memória evitando carregar todas as linhas do arquivo.
    - Iterar linha a linha do arquivo.
"""

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)

"""
Explicação do código:

class MeuIterador:
    # Cria a classe chamada MeuIterador
    class MeuIterador:

    def __init__(self, numeros: list[int]):
        # O método __init__ é executado automaticamente quando
        # criamos um objeto da classe.
        #
        # numeros: list[int] significa que esperamos receber
        # uma lista contendo números inteiros.
        #
        # Exemplo:
        # MeuIterador([1, 2, 3])

        self.numeros = numeros
        # Guarda a lista recebida dentro do objeto.
        # self.numeros passa a ser [1, 2, 3], por exemplo.

        self.contador = 0
        # Cria um contador para saber em qual posição da lista
        # estamos atualmente.
        #
        # Como listas começam no índice 0:
        # contador = 0 -> primeiro elemento
        # contador = 1 -> segundo elemento
        # contador = 2 -> terceiro elemento


    def __iter__(self):
        # O método __iter__ faz com que o objeto possa ser usado
        # como um iterador.
        #
        # Quando o Python encontra:
        #
        # for i in MeuIterador(...):
        #
        # ele chama esse método.

        return self
        # Retorna o próprio objeto como iterador.
        #
        # Ou seja, o próprio MeuIterador será responsável por
        # fornecer os próximos valores.


    def __next__(self):
        # O método __next__ é responsável por fornecer
        # o próximo elemento do iterador.

        try:
            # O try permite tentar executar um código que
            # pode gerar uma exceção.

            numero = self.numeros[self.contador]
            # Pega o número que está na posição indicada pelo contador.
            #
            # Primeira execução:
            # self.numeros[0] -> 1
            #
            # Segunda execução:
            # self.numeros[1] -> 2
            #
            # Terceira execução:
            # self.numeros[2] -> 3

            self.contador += 1
            # Depois de pegar o número, aumenta o contador em 1.
            #
            # 0 -> 1
            # 1 -> 2
            # 2 -> 3

            return numero * 2
            # Retorna o número multiplicado por 2.
            #
            # 1 * 2 -> 2
            # 2 * 2 -> 4
            # 3 * 2 -> 6

        except IndexError:
            # Quando o contador chegar a 3, o Python tentará:
            #
            # self.numeros[3]
            #
            # Mas a lista [1, 2, 3] só possui os índices:
            # 0, 1 e 2.
            #
            # Portanto, ocorrerá um IndexError.
            #
            # O except captura esse erro.

            raise StopIteration
            # StopIteration informa ao Python que não existem
            # mais elementos para serem retornados.
            #
            # O for entende essa exceção como:
            # "acabou a iteração".
            #
            # Por isso o loop termina normalmente.


# Cria um objeto da classe MeuIterador e passa a lista [1, 2, 3].
#
# O for começa a iterar sobre esse objeto.
for i in MeuIterador(numeros=[1, 2, 3]):

    # A cada iteração, o valor retornado pelo __next__()
    # é colocado dentro da variável i.

    print(i)
    # Imprime o valor recebido.

"""