import tkinter as tk


class Jogo():
    def __init__(self, tentativas):
        self._tentativas = tentativas


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


def dificuldade_normal():
    jogo = Jogo(6)


def dificuldade_dificil():
    jogo = Jogo(4)


menu_dificuldades()
