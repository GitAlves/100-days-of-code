import tkinter as tk


def validador(ano: int):
    if ano % 4 == 0:
        return f'\n\n{ano} é um ano bissexto!'
    else:
        return f'\n\n{ano} não é um ano bissexto!'


janela = tk.Tk()
janela.title('Validador de anos bissextos!')
janela.geometry('400x250')

texto = tk.Label(
    text='Insira um ano qualquer: '
)
texto.grid(
    column=0,
    row=0,
    padx=5,
    pady=10
)

caixa_de_entrada = tk.Entry()
caixa_de_entrada.grid(
    column=1,
    row=0,
    padx=5,
    pady=10
)

botao_verificar = tk.Button(
    text='Verificar',
    command=validador
)
botao_verificar.grid(
    column=2,
    row=0,
    padx=5,
    pady=10
)

texto_resposta = tk.Label(text='O texto vai vir aqui ;)')
texto_resposta.grid(
    column=0,
    row=1,
    padx=5,
    pady=10,
    columnspan=3
)

janela.mainloop()
