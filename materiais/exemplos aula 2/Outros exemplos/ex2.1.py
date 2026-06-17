contador = 0# Inicializa a variável 'contador' com valor 1

# Enquanto o valor de 'contador' for menor ou igual a 5, o loop continua
while contador <= 10:
    print(f"Contador está em {contador}")  # Imprime o valor atual de 'contador'
    contador += 1  # Incrementa 'contador' em 1 para avançar no loop e evitar repetição infinita
    
    
#É uma formatação de string (por isso o f) introduzida no Python 3.6. Com ela, você pode inserir valores de variáveis ou expressões diretamente dentro da string, usando {}.