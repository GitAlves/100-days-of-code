from random import randint

tentativas = 4
numero = randint(1, 10)
while tentativas:
    numero_jogador = int(
        input(
            'Insira um número entre um e dez: '
        )
    )

    if numero_jogador > numero:
        print(f'Dica: O número é menor que {numero_jogador}.')
    else:
        print(f'O número é maior que {numero_jogador}.')

    if numero_jogador == numero:
        print(f'\n{numero_jogador} era o número certo. Parabéns!')
        break

    tentativas -= 1

if tentativas == 0 and numero_jogador != numero:
    print('\nAs suas chances acabaram!')
    print(f'O número sorteado foi {numero}.')
