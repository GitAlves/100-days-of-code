from random import randint


def jogar_dado(lados):
    return randint(0, lados)


quant_lados = int(input('\n\nQuantos lados o dado vai ter: '))

resp = 'N'
while resp != 'S':
    print(f'\n\nNúmero sorteado: {jogar_dado(quant_lados)}')

    resp = input('Gostaria de encerrar o programa [S/N]: ')

print('\n\nAté mais!\n\n')
