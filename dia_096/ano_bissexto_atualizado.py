import tkinter as tk
from datetime import datetime


def validador():
    ano = int(caixa_de_entrada.get())
    verbo = comparar_ano(ano)

    if ano % 4 == 0:
        texto_resposta.config(
            text=f'O ano {ano} {verbo} bissexto!'
        )
    else:
        texto_resposta.config(
            text=f'O ano {ano} não {verbo} bissexto!'
        )


def comparar_ano(ano):
    ano_atual = datetime.now()

    if ano == ano_atual.year:
        return 'é'
    elif ano < ano_atual.year:
        return 'foi'
    else:
        return 'será'


def apenas_numeros(caracter):
    return caracter.isdigit() or caracter == ''


janela = tk.Tk()
janela.title('Validador de anos bissextos!')
janela.geometry('350x250')

texto = tk.Label(
    text='Insira um ano qualquer: '
)
texto.grid(
    column=0,
    row=0,
    padx=5,
    pady=50
)

validacao = (janela.register(apenas_numeros), '%P')

caixa_de_entrada = tk.Entry(
    justify='center',
    validate='key',
    validatecommand=validacao
)
caixa_de_entrada.grid(
    column=1,
    row=0,
    padx=5,
    pady=50
)

botao_verificar = tk.Button(
    text='Verificar',
    command=validador
)
botao_verificar.grid(
    column=2,
    row=0,
    padx=5,
    pady=50
)

texto_resposta = tk.Label(text='')
texto_resposta.grid(
    column=0,
    row=1,
    padx=5,
    pady=10,
    columnspan=3
)

janela.mainloop()
