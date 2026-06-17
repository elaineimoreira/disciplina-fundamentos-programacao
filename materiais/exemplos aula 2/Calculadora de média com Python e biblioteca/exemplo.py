import tkinter as tk

def calcular_media():
    nota1 = float(campo_nota1.get())
    nota2 = float(campo_nota2.get())

    media = (nota1 + nota2) / 2

    resultado.config(text=f"Média: {media}")

janela = tk.Tk()
janela.title("Calculadora de Média")

tk.Label(janela, text="Nota 1").pack()
campo_nota1 = tk.Entry(janela)
campo_nota1.pack()

tk.Label(janela, text="Nota 2").pack()
campo_nota2 = tk.Entry(janela)
campo_nota2.pack()

tk.Button(janela, text="Calcular", command=calcular_media).pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()