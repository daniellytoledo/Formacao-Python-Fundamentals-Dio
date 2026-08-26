import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar a função")
        return resultado
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá, mundo, {nome}!")

print(ola_mundo.__name__)

"""
Explicando o código:

import functools
# Importa o módulo functools, que possui várias ferramentas
# para trabalhar com funções.
#
# Neste exemplo, vamos usar functools.wraps.


def meu_decorador(funcao):
    # Cria uma função chamada meu_decorador.
    #
    # funcao é o parâmetro que vai receber a função que queremos
    # decorar.
    #
    # Por exemplo, mais abaixo teremos:
    #
    # @meu_decorador
    # def ola_mundo(...):
    #
    # Nesse caso, a função ola_mundo será recebida aqui
    # através do parâmetro "funcao".

    @functools.wraps(funcao)
    # functools.wraps é um decorador utilizado dentro do nosso
    # próprio decorador.
    #
    # Ele preserva informações da função original, como:
    # - __name__ (nome da função)
    # - __doc__ (documentação)
    # - __module__
    #
    # Isso é importante porque, sem wraps, a função decorada
    # poderia passar a ter o nome "envelope".

    def envelope(*args, **kwargs):
        # Cria uma nova função chamada envelope.
        #
        # Essa função vai "envolver" a função original.
        #
        # *args recebe argumentos posicionais.
        #
        # Exemplo:
        # ola_mundo("Dani", "teste")
        #
        # "Dani" e "teste" poderiam ser recebidos por args.
        #
        # **kwargs recebe argumentos nomeados.
        #
        # Exemplo:
        # ola_mundo(nome="Dani", outro_argumento="teste")
        #
        # Esses argumentos seriam recebidos por kwargs.

        print("Faz algo antes de executar a função")
        # Executa alguma coisa ANTES da função original.

        resultado = funcao(*args, **kwargs)
        # Aqui finalmente executamos a função original.
        #
        # funcao é a função que foi passada para o decorador.
        #
        # *args e **kwargs repassam os argumentos recebidos
        # para a função original.
        #
        # O resultado retornado pela função é armazenado
        # na variável resultado.

        print("Faz algo depois de executar a função")
        # Executa alguma coisa DEPOIS da função original.

        return resultado
        # Retorna o resultado produzido pela função original.

    return envelope
    # O decorador retorna a função envelope.
    #
    # A partir desse momento, a função original passa a ser
    # "envolvida" pelo envelope.


@meu_decorador
# Isso é uma forma mais curta de escrever:
#
# ola_mundo = meu_decorador(ola_mundo)
#
# Ou seja, Python pega a função ola_mundo e passa para
# meu_decorador.


def ola_mundo(nome, outro_argumento):
    # Cria a função ola_mundo.
    #
    # Ela recebe dois argumentos:
    # nome
    # outro_argumento

    print(f"Olá, mundo, {nome}!")
    # Exibe uma mensagem utilizando o valor de nome.
    #
    # Observe que outro_argumento não está sendo utilizado
    # dentro da função.


print(ola_mundo.__name__)
# __name__ contém o nome da função.
#
# Como usamos:
#
# @functools.wraps(funcao)
#
# o Python preserva o nome da função original.
#
# Portanto, o resultado será:
#
# ola_mundo

"""