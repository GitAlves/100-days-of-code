from random import choice as ch
from time import sleep as sl


def vez_da_maquina():
    return ch(['pedra', 'papel', 'tesoura'])


def escolhendo_pedra(jogada_maquina):
    if jogada_maquina == 'pedra':
        return 'empate'
    elif jogada_maquina == 'papel':
        return 'derrota'
    else:
        return 'vitória'


def escolhendo_papel(jogada_maquina):
    if jogada_maquina == 'pedra':
        return 'vitória'
    elif jogada_maquina == 'papel':
        return 'empate'
    else:
        return 'derrota'


def escolhendo_tesoura(jogada_maquina):
    if jogada_maquina == 'pedra':
        return 'derrota'
    elif jogada_maquina == 'papel':
        return 'vitória'
    else:
        return 'empate'


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
            jogada_da_maquina = vez_da_maquina()

            print('\nConstatando o resultado...\n')
            sl(3)

            if jogada_do_usuario == 1:
                resultado = escolhendo_pedra(jogada_da_maquina)
            elif jogada_do_usuario == 2:
                resultado = escolhendo_papel(jogada_da_maquina)
            elif jogada_do_usuario == 3:
                resultado = escolhendo_tesoura(jogada_da_maquina)
            else:
                print('Para esta opção não há função!')

            if resultado == 'vitória':
                pontuacao_jogador += 1
                print('Você venceu!')
            elif resultado == 'derrota':
                pontuacao_maquina += 1
                print('A máquina ganhou dessa vez :(')
            else:
                print('Empatou? A pontuação fica com a banca!!!')

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
