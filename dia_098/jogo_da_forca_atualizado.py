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
        self.palavra_jogador = '_ ' * len(self._palavra)

        self.janela_jogo = tk.Toplevel()
        self.janela_jogo.title('Acerte a palavra')
        self.janela_jogo.geometry('380x250+60+60')

        self.texto_dica = tk.Label(
            self.janela_jogo,
            text='Dica: É uma fruta!!!',
            font=('Arial', 12, 'bold')
        )
        self.texto_dica.grid(
            column=0,
            row=0,
            padx=(80, 5),
            pady=10,
            columnspan=3
        )

        texto_letras_erradas = tk.Label(
            self.janela_jogo,
            text='Letras erradas: ',
            font=('Arial', 12, 'bold')
        )
        texto_letras_erradas.grid(
            column=0,
            row=1,
            padx=5,
            pady=10
        )

        self.letras_erradas = tk.Label(
            self.janela_jogo,
            text=self.lista_letras_erradas,
            font=('Arial', 12, 'bold'),
        )
        self.letras_erradas.grid(
            column=1,
            row=1,
            padx=5,
            pady=10
        )

        self.palavra_misteriosa = tk.Label(
            self.janela_jogo,
            text=self.palavra_jogador,
            font=('Arial', 12, 'bold')
        )
        self.palavra_misteriosa.grid(
            column=0,
            row=2,
            padx=(80, 5),
            pady=(10, 30),
            columnspan=3
        )

        texto_chute = tk.Label(
            self.janela_jogo,
            text='Chute uma letra:',
            font=('Arial', 12, 'bold')
        )
        texto_chute.grid(
            column=0,
            row=3,
            padx=(5, 0),
            pady=10
        )

        self.campo_chute = tk.Entry(
            self.janela_jogo,
            font=('Arial', 10)
        )
        self.campo_chute.grid(
            column=1,
            row=3,
            padx=(0, 5),
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

        self.texto_tentativas = tk.Label(
            self.janela_jogo,
            text=f'Tentativas: {self._tentativas}',
            font=('Arial', 12, 'bold')
        )
        self.texto_tentativas.grid(
            column=0,
            row=4,
            padx=(80, 0),
            pady=10,
            columnspan=3
        )

        self.janela_jogo.mainloop()

    def sortear_palavra(self):
        with open('dia_098/frutas.txt') as arq:
            rascunho = arq.readlines()
            return ch(rascunho).split('\n')[0].upper()

    def verificar_letra(self):
        letra_usuario = str(self.campo_chute.get().upper())
        palavra_usuario = list(self.palavra_jogador.replace(' ', ''))

        if letra_usuario in self._palavra:
            for posicao, letra in enumerate(self._palavra):
                if letra_usuario == letra:
                    palavra_usuario[posicao] = letra_usuario

            self.palavra_jogador = ' '.join(palavra_usuario)
            self.palavra_misteriosa.config(
                text=self.palavra_jogador
            )

            if self.palavra_jogador.replace(' ', '') == self._palavra:
                self.vitoria()
        else:
            self._tentativas -= 1
            self.lista_letras_erradas += letra_usuario

            self.letras_erradas.config(
                text=self.lista_letras_erradas
            )

            self.texto_tentativas.config(
                text=f'Tentativas: {self._tentativas}'
            )

            if self._tentativas == 0:
                self.derrota()

    def vitoria(self):
        self.janela_jogo.withdraw()
        self.tela_vitoria = tk.Toplevel()
        self.tela_vitoria.title('Você venceu!')
        self.tela_vitoria.geometry('250x150')

        mensagem_vitoria = tk.Label(
            self.tela_vitoria,
            text='Parabéns!',
            font=('Arial', 15, 'bold')
        )
        mensagem_vitoria.grid(
            column=0,
            row=0,
            padx=(80, 100),
            pady=(40, 20),
            columnspan=2
        )

        botao_reiniciar = tk.Button(
            self.tela_vitoria,
            text='Reiniciar',
            command=self.reiniciar_jogo_vencido
        )
        botao_reiniciar.grid(
            column=0,
            row=1,
            padx=5,
            pady=10
        )

        botao_sair = tk.Button(
            self.tela_vitoria,
            text='Sair',
            command=self.sair_do_jogo
        )
        botao_sair.grid(
            column=1,
            row=1,
            padx=(5, 40),
            pady=10
        )

        self.tela_vitoria.mainloop()

    def derrota(self):
        self.janela_jogo.withdraw()
        self.tela_derrota = tk.Toplevel()
        self.tela_derrota.title('Game over :(')
        self.tela_derrota.geometry('300x150')

        mensagem_derrota = tk.Label(
            self.tela_derrota,
            text=f'Não foi dessa vez!!!\nA palavra era "{self._palavra}".',
            font=('Arial', 11, 'bold')
        )
        mensagem_derrota.grid(
            column=0,
            row=0,
            padx=(60, 60),
            pady=20,
            columnspan=2
        )

        botao_reiniciar = tk.Button(
            self.tela_derrota,
            text='Reiniciar',
            command=self.reiniciar_jogo_perdido
        )
        botao_reiniciar.grid(
            column=0,
            row=1,
            padx=(5, 15),
            pady=10
        )

        botao_sair = tk.Button(
            self.tela_derrota,
            text='Sair',
            command=self.sair_do_jogo
        )
        botao_sair.grid(
            column=1,
            row=1,
            padx=(15, 5),
            pady=10
        )

        self.tela_derrota.mainloop()

    def reiniciar_jogo_vencido(self):
        self.tela_vitoria.destroy()
        self.janela_jogo.destroy()
        self.janela_menu.deiconify()

    def reiniciar_jogo_perdido(self):
        self.tela_derrota.destroy()
        self.janela_jogo.destroy()
        self.janela_menu.deiconify()

    def sair_do_jogo(self):
        self.janela_menu.destroy()


if __name__ == '__main__':
    janela = tk.Tk()
    jogo = Jogo(janela)
    jogo.menu_dificuldades()
    janela.mainloop()
