#Organizando anos de publicação dos livros

# Lista com anos dos livros
anos = [2018, 2022, 2015, 2020]

# Percorre cada posição da lista
for i in range(len(anos)):

    # Assume que o menor número está na posição atual
    menor = i

    # Procura um número menor nas próximas posições
    for j in range(i + 1, len(anos)):

        # Se encontrar um valor menor
        if anos[j] < anos[menor]:

            # Guarda a posição do menor valor
            menor = j

    # Troca o valor atual pelo menor encontrado
    anos[i], anos[menor] = anos[menor], anos[i]

# Exibe a lista organizada
print(anos)