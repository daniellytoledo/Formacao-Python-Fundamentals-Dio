"""
Funções de decoração com argumentos

Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais e de palavras-chave.
"""

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return envelope

@duplicar 
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")

aprender("Python")

# ---

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar a função")

    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá, mundo, {nome}!")

ola_mundo("João", 1000) # 1000 sendo só um exemplo de um segundo argumento

"""
Retornando valores de funções decoradas

O decorador pode decidir se retorna o valor da função decorada ou não. Para que o valor seja retornado, a função de envelope deve retornar o valor da função decorada.
"""

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a função")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar a função")
        return resultado
    return envelope

resultado = ola_mundo("João", 1000)
print(resultado)