import tkinter as tk
from random import choice as ch


class Jogo():
    def __init__(self, janela):
        self._janela_base = janela
        self._tentativas = 0
        self._palavra = ''
        self.palavra_jogador = ''
        self.lista_letras_erradas = ''

    def menu_dificuldades(self):
        self.janela_menu = self._janela_base
        self.janela_menu.title('Escolha a dificuldade')
        self.janela_menu.geometry('300x250')

        botao_facil = tk.Button(
            self.janela_menu,
            text='Fácil - Acerte a palavra em 10 tentativas',
            command=self.dificuldade_facil
        )
        botao_facil.grid(
            column=0,
            row=0,
            padx=40,
            pady=(50, 10)
        )

        botao_normal = tk.Button(
            self.janela_menu,
            text='Normal - Acerte a palavra em 6 tentativas',
            command=self.dificuldade_normal
        )
        botao_normal.grid(
            column=0,
            row=1,
            padx=5,
            pady=10
        )

        botao_dificil = tk.Button(
            self.janela_menu,
            text='Difícil - Acerte a palavra em 4 tentativas',
            command=self.dificuldade_dificil
        )
        botao_dificil.grid(
            column=0,
            row=2,
            padx=5,
            pady=10
        )

        self.janela_menu.mainloop()

    def dificuldade_facil(self):
        self.janela_menu.withdraw()
        self._tentativas = 10
        self.tela_jogo()

    def dificuldade_normal(self):
        self.janela_menu.withdraw()
        self._tentativas = 6
        self.tela_jogo()

    def dificuldade_dificil(self):
        self.janela_menu.withdraw()
        self._tentativas = 4
        self.tela_jogo()

    def tela_jogo(self):
        self._palavra = self.sortear_palavra()
        self.palavra_jogador = '_' * len(self._palavra)

        self.janela_jogo = tk.Toplevel()
        self.janela_jogo.title('Acerte a palavra')
        self.janela_jogo.geometry('300x230')

        self.texto_tentativas = tk.Label(
            self.janela_jogo,
            text=f'Tentativas: {self._tentativas}'
        )
        self.texto_tentativas.grid(
            column=0,
            row=0,
            padx=(100, 0),
            pady=10,
            columnspan=3
        )

        texto_letras_erradas = tk.Label(
            self.janela_jogo,
            text='Letras erradas: '
        )
        texto_letras_erradas.grid(
            column=0,
            row=1,
            padx=5,
            pady=10
        )

        self.letras_erradas = tk.Label(
            self.janela_jogo,
            text=self.lista_letras_erradas
        )
        self.letras_erradas.grid(
            column=1,
            row=1,
            padx=5,
            pady=10
        )

        self.palavra_misteriosa = tk.Label(
            self.janela_jogo,
            text=self.palavra_jogador
        )
        self.palavra_misteriosa.grid(
            column=0,
            row=2,
            padx=5,
            pady=10,
            columnspan=2
        )

        texto_chute = tk.Label(
            self.janela_jogo,
            text='Chute uma letra'
        )
        texto_chute.grid(
            column=0,
            row=3,
            padx=5,
            pady=10
        )

        self.campo_chute = tk.Entry(
            self.janela_jogo,
        )
        self.campo_chute.grid(
            column=1,
            row=3,
            padx=5,
            pady=10
        )

        botao_verificar = tk.Button(
            self.janela_jogo,
            text='Verificar',
            command=self.verificar_letra
        )
        botao_verificar.grid(
            column=2,
            row=3,
            padx=5,
            pady=10,
            columnspan=2
        )

        botao_sair = tk.Button(
            self.janela_jogo,
            text='Sair',
            command=quit
        )
        botao_sair.grid(
            column=0,
            row=4,
            padx=(100, 0),
            pady=10,
            columnspan=3
        )

        self.janela_jogo.mainloop()

    def verificar_letra(self):
        ...


if __name__ == '__main__':
    janela = tk.Tk()
    jogo = Jogo(janela)
    jogo.menu_dificuldades()
    janela.mainloop()
