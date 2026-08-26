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