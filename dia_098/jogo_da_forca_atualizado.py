import tkinter as tk
from random import choice as ch


class Jogo():
    def __init__(self, tentativas):
        self._tentativas = tentativas
        self._palavra = ''

    def tela_jogo(self):
        tela = tk.Tk()
        tela.title('Acerte a palavra')
        tela.geometry('600x400')

        texto_tentativas = tk.Label(
            tela,
            text=f'Tentativas: {self._tentativas}'
        )
        texto_tentativas.grid(
            column=0,
            row=0,
            padx=5,
            pady=10,
            columnspan=2
        )

        texto_letras_erradas = tk.Label(
            tela,
            text='Letras erradas: '
        )
        texto_letras_erradas.grid(
            column=0,
            row=1,
            padx=5,
            pady=10,
            columnspan=2
        )

        texto_chute = tk.Label(
            tela,
            text='Chute uma letra'
        )
        texto_chute.grid(
            column=0,
            row=2,
            padx=5,
            pady=10
        )

        campo_chute = tk.Entry(
            tela,
        )
        campo_chute.grid(
            column=1,
            row=2,
            padx=5,
            pady=10
        )

        botao_verificar = tk.Button(
            tela,
            text='Verificar'
        )
        botao_verificar.grid(
            column=0,
            row=3,
            padx=5,
            pady=10,
            columnspan=2
        )

        tela.mainloop()

    def sortear_palavra(self):
        with open('frutas.txt') as arq:
            rascunho = arq.readlines()
            self._palavra = ch(rascunho).split('\n')[0].upper()


def menu_dificuldades():
    menu = tk.Tk()
    menu.title('Escolha a dificuldade')
    menu.geometry('300x250')

    botao_facil = tk.Button(
        menu,
        text='Fácil - Acerte a palavra em 10 tentativas',
        command=dificuldade_facil
    )
    botao_facil.grid(
        column=0,
        row=0,
        padx=40,
        pady=(50, 10)
    )

    botao_normal = tk.Button(
        menu,
        text='Normal - Acerte a palavra em 6 tentativas',
        command=dificuldade_normal
    )
    botao_normal.grid(
        column=0,
        row=1,
        padx=5,
        pady=10
    )

    botao_dificil = tk.Button(
        menu,
        text='Difícil - Acerte a palavra em 4 tentativas',
        command=dificuldade_dificil
    )
    botao_dificil.grid(
        column=0,
        row=2,
        padx=5,
        pady=10
    )

    menu.mainloop()


def dificuldade_facil():
    jogo = Jogo(10)
    jogo.tela_jogo()


def dificuldade_normal():
    jogo = Jogo(6)
    jogo.tela_jogo()


def dificuldade_dificil():
    jogo = Jogo(4)
    jogo.tela_jogo()


menu = menu_dificuldades()
