"""
Podemos usar write() ou writelines() para escrever em um arquivo. Lembre-se, no entanto, de abrir o arquivo no modo correto.
"""

# Criando um arquivo com write()
file = open(
    r"C:\Users\Msi\Desktop\ESTUDOS\CURSOS\Dio\Formacao_Python_Fundamentals\Formacao-Python-Fundamentals-Dio\Modulo4-Decoradores-Iteradores-Manipulacao\03_manipulando_dados_python/teste.txt", "w"
)

file.write("Ola, mundo!")
file.writelines("Python") # o writelines escreve uma letra por letra, o que não faz muito sentido
file.writelines(["\n", "escrevendo ", "um ", "novo ", "texto."])
file.close()

