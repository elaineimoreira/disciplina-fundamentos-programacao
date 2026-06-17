# --------------------------------------------------
# EXEMPLO DE ALGORITMO EM PYTHON
# Cálculo de média escolar com validação do nome
# --------------------------------------------------

# Solicita ao usuário que digite o nome do aluno.
# O valor digitado será armazenado na variável "nome".
nome = input("Digite o nome do aluno: ")

# Enquanto o nome for inválido, o programa continuará pedindo um novo nome.
#
# nome.replace(" ", "")
# Remove todos os espaços do texto.
#
# Exemplo:
# "Maria Silva" → "MariaSilva"
#
# isalpha()
# Verifica se todos os caracteres são letras.
#
# not
# Inverte o resultado:
# True vira False
# False vira True
#
# Portanto:
# enquanto NÃO for composto apenas por letras,
# continue repetindo.
while not nome.replace(" ", "").isalpha():

    # Exibe uma mensagem de erro para o usuário.
    print("Erro: o nome deve conter apenas letras.")

    # Solicita novamente o nome.
    nome = input("Digite o nome do aluno novamente: ")

# Solicita a primeira nota.
#
# input() retorna texto.
# float() converte esse texto para número decimal.
#
# Exemplo:
# "8.5" → 8.5
nota1 = float(input("Digite a primeira nota: "))

# Solicita a segunda nota e converte para número decimal.
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média aritmética.
#
# Primeiro soma as duas notas.
# Depois divide o resultado por 2.
#
# Exemplo:
# (8 + 10) / 2 = 9
media = (nota1 + nota2) / 2

# Estrutura de decisão.
#
# Verifica se a média é maior ou igual a 6.
#
# Se for:
#   aluno aprovado
#
# Caso contrário:
#   aluno reprovado
if media >= 6:

    # Armazena a situação do aluno.
    situacao = "Aprovado"

else:

    # Armazena a situação do aluno.
    situacao = "Reprovado"

# Exibe uma linha em branco antes do resultado.
#
# \n significa "quebra de linha".
print("\nRESULTADO")

# Exibe o nome do aluno.
print("Aluno:", nome)

# Exibe a média calculada.
print("Média:", media)

# Exibe a situação final.
print("Situação:", situacao)