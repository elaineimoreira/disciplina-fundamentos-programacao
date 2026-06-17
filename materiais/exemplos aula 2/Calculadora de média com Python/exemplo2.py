# Entrada de dados

nome = input("Digite o nome do aluno: ")

# Validação do nome
while not nome.replace(" ", "").isalpha():
    print("Erro: o nome deve conter apenas letras.")
    nome = input("Digite o nome do aluno novamente: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento
media = (nota1 + nota2) / 2

# Estrutura de decisão
if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Saída de dados
print("\nRESULTADO")
print("Aluno:", nome)
print("Média:", media)
print("Situação:", situacao)