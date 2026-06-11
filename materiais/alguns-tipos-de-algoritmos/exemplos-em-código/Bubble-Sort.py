#Organizando notas de alunos

# Lista de notas
notas = [8.5, 6.0, 9.0, 7.5]

# Repete o processo várias vezes
for i in range(len(notas)):

    # Percorre a lista comparando elementos vizinhos
    for j in range(len(notas) - 1):

        # Se o número da esquerda for maior que o da direita
        if notas[j] > notas[j + 1]:

            # Troca os dois de lugar
            notas[j], notas[j + 1] = notas[j + 1], notas[j]

# Mostra a lista organizada
print(notas)