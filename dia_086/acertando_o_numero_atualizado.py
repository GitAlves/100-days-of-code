from random import randint
import tkinter as tk
from tkinter import messagebox


class JogoNumeroAleatorio:
    def __init__(self, janela):
        self.tela_menu = janela
        self.janela_jogo = janela
        self.tela_vitoria = janela
        self.tela_derrota = janela

    def menu(self):
        self.tela_menu.title('Escolha a dificuldade!')
        self.tela_menu.geometry('350x300')

        texto_dificuldade = tk.Label(self.tela_menu, text='Escolha a dificuldade:')  # noqa: E501;
        texto_dificuldade.grid(
            column=0,
            row=0,
            padx=30,
            pady=10,
            columnspan=2
        )

        facil = tk.Button(
            self.tela_menu,
            text='Fácil - Acerte um número entre 1 e 10 em 4 tentativas',
            command=self.comecar_jogo_facil
        )
        facil.grid(
            column=0,
            row=1,
            padx=30,
            pady=10,
            columnspan=2
        )

        normal = tk.Button(
            self.tela_menu,
            text='Normal - Acerte um número entre 1 e 30 em 6 tentativas',
            command=self.comecar_jogo_normal
        )
        normal.grid(
            column=0,
            row=2,
            padx=30,
            pady=10,
            columnspan=2
        )

        dificil = tk.Button(
            self.tela_menu,
            text='Difícil - Acerte o número entre 1 e 50 em 8 tentativas',
            command=self.comecar_jogo_dificil
        )
        dificil.grid(
            column=0,
            row=3,
            padx=30,
            pady=10,
            columnspan=2
        )

    def comecar_jogo_facil(self):
        self.tela_menu.withdraw()
        self.jogo(1, 10, 4)

    def comecar_jogo_normal(self):
        self.tela_menu.withdraw()
        self.jogo(1, 30, 6)

    def comecar_jogo_dificil(self):
        self.tela_menu.withdraw()
        self.jogo(1, 50, 8)

    def jogo(self, num_inicio, num_fim, tentativas):
        self.janela_jogo = tk.Toplevel()
        self.janela_jogo.title('Adivinhe o número!')
        self.janela_jogo.geometry('300x180')

        self.numero_aleatorio = randint(num_inicio, num_fim)
        self.tentativas = tentativas

        self.texto_auxilio = tk.Label(self.janela_jogo, text=f'Adivinhe um número entre {num_inicio} e {num_fim}:')  # noqa: E501;
        self.texto_auxilio.grid(
            column=0,
            row=0,
            padx=50,
            pady=10
        )

        self.entry = tk.Entry(self.janela_jogo)
        self.entry.grid(
            column=0,
            row=1,
            padx=50,
            pady=10
        )

        self.botao_verificar = tk.Button(self.janela_jogo, text='Verificar', command=self.checar_numero)  # noqa: E501;
        self.botao_verificar.grid(
            column=0,
            row=2,
            padx=50,
            pady=10
        )

        self.campo_tentativas = tk.Label(self.janela_jogo, text=f'Tentativas restantes: {self.tentativas}')  # noqa: E501;
        self.campo_tentativas.grid(
            column=0,
            row=3,
            padx=50,
            pady=10
        )

    def checar_numero(self):
        try:
            numero_jogador = int(self.entry.get())
        except ValueError:
            messagebox.showerror('Erro', 'Apenas números inteiros são permitidos!')  # noqa: E501;
            return

        if 1 > numero_jogador < 100:
            messagebox.showerror('Erro', 'Por favor insira um número entre 1 e 10')  # noqa: E501;
            return

        self.tentativas -= 1
        self.campo_tentativas.config(text=f'Tentativas restantes: {self.tentativas}')  # noqa: E501;

        if numero_jogador == self.numero_aleatorio:
            messagebox.showinfo('Parabéns', 'Você acertou!')
            self.vitoria()
        elif self.tentativas == 0:
            messagebox.showinfo('Fim de jogo', f'Você perdeu! O número era {self.numero_aleatorio}')  # noqa: E501;
            self.derrota()
        elif numero_jogador < self.numero_aleatorio:
            messagebox.showinfo('Dica', f'O número é maior que {numero_jogador}!')  # noqa: E501;
        else:
            messagebox.showinfo('Dica', f'Dica: O número é menor que {numero_jogador}!')  # noqa: E501;

    def vitoria(self):
        self.janela_jogo.withdraw()
        self.tela_vitoria = tk.Toplevel()
        self.tela_vitoria.title('Acertou o número!!!')
        self.tela_vitoria.geometry('300x100')

        mensagem_vitoria = tk.Label(
            self.tela_vitoria,
            text='Parabéns'
        )
        mensagem_vitoria.grid(
            column=0,
            row=0,
            padx=120,
            pady=10,
            columnspan=2
        )

        botao_reinicio = tk.Button(
            self.tela_vitoria,
            text='Reiniciar',
            command=self.restartar_jogo_vencido
        )
        botao_reinicio.grid(
            column=0,
            row=1,
            padx=5,
            pady=10
        )

        botao_sair = tk.Button(
            self.tela_vitoria,
            text='Sair',
            command=self.fechar_jogo
        )
        botao_sair.grid(
            column=1,
            row=1,
            padx=5,
            pady=10
        )

    def derrota(self):
        self.janela_jogo.withdraw()
        self.tela_derrota = tk.Toplevel()
        self.tela_derrota.title('Não foi dessa vez :(')
        self.tela_derrota.geometry('300x100')

        mensagem_derrota = tk.Label(
            self.tela_derrota,
            text='Game over'
        )
        mensagem_derrota.grid(
            column=0,
            row=0,
            padx=120,
            pady=10,
            columnspan=2
        )

        botao_reinicio = tk.Button(
            self.tela_derrota,
            text='Reiniciar',
            command=self.restartar_jogo_perdido
        )
        botao_reinicio.grid(
            column=0,
            row=1,
            padx=5,
            pady=10
        )

        botao_sair = tk.Button(
            self.tela_derrota,
            text='Sair',
            command=self.fechar_jogo
        )
        botao_sair.grid(
            column=1,
            row=1,
            padx=5,
            pady=10
        )

    def restartar_jogo_vencido(self):
        self.tela_vitoria.destroy()
        self.janela_jogo.destroy()
        self.tela_menu.deiconify()
        self.menu()

    def restartar_jogo_perdido(self):
        self.tela_derrota.destroy()
        self.janela_jogo.destroy()
        self.tela_menu.deiconify()
        self.menu()

    def fechar_jogo(self):
        self.tela_menu.destroy()


if __name__ == '__main__':
    janela = tk.Tk()
    jogo = JogoNumeroAleatorio(janela)
    jogo.menu()
    janela.mainloop()
