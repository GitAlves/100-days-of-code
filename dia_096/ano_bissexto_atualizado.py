import tkinter as tk
from datetime import datetime


def validador():
    try:
        ano = int(caixa_de_entrada.get())
    except ValueError:
        pass
    else:
        verbo = comparar_ano(ano)
        caixa_de_entrada.delete(0, 'end')

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


def sair():
    janela.destroy()


janela = tk.Tk()
janela.title('Validador de anos bissextos!')
janela.geometry('350x250')

texto = tk.Label(
    text='Insira um ano para validar: '
)
texto.grid(
    column=0,
    row=0,
    padx=(10, 0),
    pady=(50, 30)
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
    padx=0,
    pady=(50, 30)
)

botao_verificar = tk.Button(
    text='Verificar',
    command=validador
)
botao_verificar.grid(
    column=2,
    row=0,
    padx=(3, 10),
    pady=(50, 30)
)

texto_resposta = tk.Label(text='')
texto_resposta.grid(
    column=0,
    row=1,
    padx=5,
    pady=(20, 40),
    columnspan=3
)

botao_sair = tk.Button(
    text='Sair',
    command=sair
)
botao_sair.grid(
    column=0,
    row=2,
    padx=5,
    pady=10,
    columnspan=3
)

janela.mainloop()
