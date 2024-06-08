from random import choice as ch
import tkinter as tk


def lembrete_tentativas(numero):
    return f'\n--------- TENTATIVAS: {numero} ---------\n'


palavra = ch(
    [
        'uva',
        'banana',
        'morango',
        'figo',
        'amora',
        'acerola',
        'marmelo',
        'abacaxi'
    ]
)
palavra_escondida = '-' * len(palavra)

tentativas = 10
print(lembrete_tentativas(tentativas))

while tentativas:
    print(palavra_escondida)

    chute = input('\nChute uma letra: ')

    if chute in palavra:
        print('\nLETRA ENCONTRADA!!!\n')

        rascunho = list(palavra_escondida)

        for posicao, letra in enumerate(palavra):
            if letra == chute:
                rascunho[posicao] = letra

        palavra_escondida = ''.join(rascunho)
    else:
        tentativas -= 1
        print('Errou!')
        print(lembrete_tentativas(tentativas))

    if palavra == palavra_escondida:
        print('Meus parabéns! Você ganhou.')
        break

if tentativas == 0:
    print(f'Game over!\nA palavra era "{palavra}".')


def menu_dificuldades():
    menu = tk.Tk()
    menu.title('Escolha a dificuldade')
    menu.geometry('300x250')

    botao_facil = tk.Button(
        text='Fácil - Acerte a palavra em 10 tentativas',
    )
    botao_facil.grid(
        column=0,
        row=0,
        padx=40,
        pady=(50, 10)
    )

    botao_medio = tk.Button(
        menu,
        text='Normal - Acerte a palavra em 6 tentativas'
    )
    botao_medio.grid(
        column=0,
        row=1,
        padx=5,
        pady=10
    )

    botao_dificil = tk.Button(
        menu,
        text='Difícil - Acerte a palavra em 4 tentativas'
    )
    botao_dificil.grid(
        column=0,
        row=2,
        padx=5,
        pady=10
    )

    menu.mainloop()


menu_dificuldades()
