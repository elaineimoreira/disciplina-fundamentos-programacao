nota = 6.6  # Atribuímos à variável 'nota' o valor 7

# 'if' é usado para começar uma verificação condicional.
# Ele checa se a condição logo após ele é verdadeira.
if nota == 10:
    # Se a condição do 'if' for verdadeira (nota igual a 10),
    # executa este bloco de código.
    print("Nota máxima! Excelente trabalho!")

# 'elif' significa "else if" (senão se) e é usado para verificar outra condição
# se a condição do 'if' anterior não for verdadeira.
elif 8 <= nota <= 9:
    # Se a nota estiver entre 8 e 9, executa este bloco.
    print("Muito bom!")

elif 6 <= nota <= 7:
    # Outra condição verificada se as anteriores forem falsas.
    # Aqui, se a nota estiver entre 6 e 7, executa este bloco.
    print("Bom, mas pode melhorar.")

elif 0 <= nota <= 5:
    # Mais uma condição para checar se a nota está entre 0 e 5.
    print("Insatisfatório. É preciso estudar mais.")

# 'else' é a última opção, que será executada caso nenhuma das condições
# anteriores seja verdadeira.
else:
    # Aqui, indica que a nota está fora do esperado (menor que 0 ou maior que 10).
    print("Nota inválida.")
