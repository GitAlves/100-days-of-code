from random import randint


class NumeroAleatorio:
    def __init__(self):
        self._numero = randint(1, 10)

    def comparar_numero(self, numero_jogador):
        return True if numero_jogador == self._numero else False

    @property
    def numero(self):
        return self._numero

    def novo_numero(self):
        self._numero = randint(1, 10)


tentativas = 4
numero = NumeroAleatorio()
resp = 'N'
while resp != 'S':
    while tentativas:
        try:
            numero_jogador = int(
                input(
                    '\n\nInsira um número entre um e dez: '
                )
            )
        except ValueError:
            print('\n\nUse números inteiros para tentar acertar o número!')
        else:
            if numero_jogador > numero.numero:
                print(f'\n\nDica: O número é menor que {numero_jogador}.')
            elif numero_jogador < numero.numero:
                print(f'\n\nO número é maior que {numero_jogador}.')

            if numero_jogador == numero.numero:
                print(f'\n\n{numero_jogador} era o número certo. Parabéns!\n\n')  # noqa: E501;
                break

            tentativas -= 1

            if tentativas == 0:
                print('\n\nAs suas chances acabaram!')
                print(f'\nO número sorteado foi {numero.numero}.\n\n')

    while True:
        resp = input('Gostaria de sair do jogo [S/N]: ')

        match resp:
            case 'S':
                break
            case 'N':
                numero.novo_numero()
                tentativas = 4
                break
            case _:
                print('\n\nUse [S] para sair ou [N] para continuar jogando\n\n')  # noqa: E501;

print('\n\nFoi um prazer!\n\n')
