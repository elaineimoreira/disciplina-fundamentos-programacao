contador = 1  # Inicializa a variável 'contador' com valor 1

# Cria um loop infinito, que só termina quando encontrar um comando 'break'
while True:
    print(f"Contador está em {contador}")  # Imprime o valor atual de 'contador'
    contador += 1  # Incrementa 'contador' em 1 para avançar no loop

    # Verifica se 'contador' passou de 5, para encerrar o loop
    if contador > 5:
        break  # Sai do loop, equivalente a terminar o 'do while'
