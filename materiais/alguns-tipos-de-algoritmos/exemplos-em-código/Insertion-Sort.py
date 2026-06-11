#Organizando horários de atendimento

# Lista de números
numeros = [5, 3, 1]

# Começa no segundo elemento
for i in range(1, len(numeros)):

    # Guarda o valor atual
    atual = numeros[i]

    # Posição anterior
    j = i - 1

    # Enquanto houver números maiores à esquerda
    while j >= 0 and numeros[j] > atual:

        # Move o número para a direita
        numeros[j + 1] = numeros[j]

        # Volta uma posição
        j -= 1

    # Coloca o número na posição correta
    numeros[j + 1] = atual

print(numeros)