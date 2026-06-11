#Organizando preços de produtos

# Função que realiza o Quick Sort
def quick_sort(lista):

    # Se a lista tiver apenas um elemento ou estiver vazia
    if len(lista) <= 1:
        return lista

    # Escolhe o primeiro elemento como pivô
    pivo = lista[0]

    # Guarda os números menores ou iguais ao pivô
    menores = [x for x in lista[1:] if x <= pivo]

    # Guarda os números maiores que o pivô
    maiores = [x for x in lista[1:] if x > pivo]

    # Organiza recursivamente os dois grupos
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

# Lista de preços
precos = [500, 100, 300, 50]

# Mostra o resultado organizado
print(quick_sort(precos))