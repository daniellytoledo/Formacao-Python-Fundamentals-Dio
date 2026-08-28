
# Recapitulando Funções em Python: são objetos de primeira classe. Isso significa que as funções podem ser passadas e usadas como argumentos.

def dizer_oi(nome):
    return f"Oi {nome}!"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntor?"

def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")

mensagem_para_guilherme(dizer_oi)
mensagem_para_guilherme(incentivar_aprender)

# --- Inner Functions

# É possível definir funções dentro de outras funções. Tais funções são chamadas de funções internas.

def pai():
    print("Escrevendo da pai() função")

    def filho1():
        print("Escrevendo da filho1() função")

    def filho2():
        print("Escvrendo da filho2() função")

    filho2()
    filho1()

pai()

# --- Retornando funções de funções

# Python também permite que você use funções como valores de retorno.

def calculadora(operacao):

    # inner functions
    def somar(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    # retornando as funções definifidas dentro do scopo
    match operacao:
        case "+":
            return somar
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div 


print(calculadora("+")(2, 2))
print(calculadora("-")(2, 2))
print(calculadora("*")(2, 2))
print(calculadora("/")(2, 2))

