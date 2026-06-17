# Importa a biblioteca Tkinter e dá a ela o apelido "tk".
# Tkinter é uma biblioteca do Python utilizada para criar interfaces gráficas.
import tkinter as tk


# Define uma função chamada calcular_media().
# Essa função será executada quando o usuário clicar no botão "Calcular".
def calcular_media():

    # Obtém o valor digitado no campo da Nota 1.
    # campo_nota1.get() retorna o valor como texto (string).
    # float() converte esse texto para número decimal.
    nota1 = float(campo_nota1.get())

    # Obtém o valor digitado no campo da Nota 2.
    # Também converte o valor para número decimal.
    nota2 = float(campo_nota2.get())

    # Calcula a média aritmética.
    # Soma as duas notas e divide o resultado por 2.
    media = (nota1 + nota2) / 2

    # Atualiza o texto do componente "resultado".
    # config() altera propriedades do componente.
    # text=f"Média: {media}" define o texto que será exibido.
    resultado.config(text=f"Média: {media}")


# Cria a janela principal da aplicação.
# Toda interface gráfica começa por uma janela principal.
janela = tk.Tk()

# Define o título da janela.
# Esse título aparece na barra superior da janela.
janela.title("Calculadora de Média")


# Cria um texto (Label) com a mensagem "Nota 1".
# O primeiro parâmetro informa que esse texto pertence à janela principal.
# pack() posiciona o componente na tela.
tk.Label(janela, text="Nota 1").pack()


# Cria uma caixa de texto (Entry) para o usuário digitar a primeira nota.
# Armazenamos essa caixa na variável campo_nota1.
campo_nota1 = tk.Entry(janela)

# Exibe a caixa de texto na janela.
campo_nota1.pack()


# Cria um texto (Label) com a mensagem "Nota 2".
tk.Label(janela, text="Nota 2").pack()


# Cria uma caixa de texto para o usuário digitar a segunda nota.
campo_nota2 = tk.Entry(janela)

# Exibe a caixa de texto na janela.
campo_nota2.pack()


# Cria um botão.
# text="Calcular" define o texto exibido no botão.
# command=calcular_media indica qual função será executada
# quando o usuário clicar no botão.
tk.Button(
    janela,
    text="Calcular",
    command=calcular_media
).pack()


# Cria um Label vazio.
# Inicialmente não exibe nenhum texto.
# Esse componente será utilizado para mostrar a média calculada.
resultado = tk.Label(janela, text="")

# Exibe o Label na janela.
resultado.pack()


# Inicia o loop principal da aplicação.
# Esse comando mantém a janela aberta e aguardando
# interações do usuário (cliques, digitação etc.).
janela.mainloop()