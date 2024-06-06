from random import choice as ch
from time import sleep as sl


def vez_da_maquina():
    return ch(['pedra', 'papel', 'tesoura'])


def escolhendo_pedra(jogada_maquina=vez_da_maquina):
    if jogada_maquina == 'pedra':
        print('Empatou? A pontuação fica com a banca!!!')
        return 0, 0
    elif jogada_maquina == 'papel':
        print('A máquina ganhou dessa vez :(')
        return 0, 1
    else:
        print('Você venceu!')
        return 1, 0


def escolhendo_papel(jogada_maquina=vez_da_maquina):
    if jogada_maquina == 'pedra':
        print('Você venceu!')
        return 1, 0
    elif jogada_maquina == 'papel':
        print('Empatou? A pontuação fica com a banca!!!')
        return 0, 0
    else:
        print('A máquina ganhou dessa vez :(')
        return 0, 1


def escolhendo_tesoura(jogada_maquina=vez_da_maquina):
    if jogada_maquina == 'pedra':
        print('A máquina ganhou dessa vez :(')
        return 0, 1
    elif jogada_maquina == 'papel':
        print('Você venceu!')
        return 1, 0
    else:
        print('Empatou? A pontuação fica com a banca!!!')
        return 0, 0


print('--------------------------------------')
print('     Pedra  X  Papel  X Tesoura       ')
print('--------------------------------------')

sair = 'N'
pontuacao_jogador = 0
pontuacao_maquina = 0
while sair != 'S':
    try:
        jogada_do_usuario = int(
            input(
                '\nDigite [1] para escolher a pedra!'
                '\nDigite [2] para escolher o papel!'
                '\nDigite [3] para escolher a tesoura!'
                '\nEscolha: '
            )
        )
    except ValueError:
        print('\n\nUse números inteiros para escolher a sua opção!')
    else:
        try:
            jogadas = {1: True, 2: True, 3: True}
            validador_de_jogada = jogadas[jogada_do_usuario]
        except KeyError:
            print('\n\nUse os números [1], [2] ou [3] para escolher a sua jogada!')  # noqa: E501;
        else:
            print('\nConstatando o resultado...\n')
            sl(3)

            match jogada_do_usuario:
                case 1:
                    resultado = list(escolhendo_pedra())
                case 2:
                    resultado = list(escolhendo_papel())
                case 3:
                    resultado = (escolhendo_tesoura())

            pontuacao_jogador += resultado[0]
            pontuacao_maquina += resultado[1]

            while True:
                sair = input('\nDeseja sair [S/N]: ')

                match sair:
                    case 'S':
                        break
                    case 'N':
                        break
                    case _:
                        pass

if pontuacao_jogador > pontuacao_maquina:
    print(f'\nVocê venceu com {pontuacao_jogador} pontos.')
elif pontuacao_maquina > pontuacao_jogador:
    print(f'\nA máquina venceu com vantagem de {pontuacao_maquina - pontuacao_jogador} pontos!')  # noqa: E501;
else:
    print('\nUé? Empatou?')
    print('Então a vitória é da máquina, pois a casa sempre tem vantagem! ;)')
