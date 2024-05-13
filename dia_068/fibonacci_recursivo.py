from termcolor import colored


def chamar_fibonacci(vezes, anterior=0, atual=1):
    print(atual, end=' ')

    atual = atual + anterior
    anterior = atual - anterior
    vezes -= 1

    if vezes > 0:
        chamar_fibonacci(vezes, anterior, atual)


resposta = 'N'
while resposta != 'S':
    try:
        quant_vezes = int(input('\n\nDigite a quantidade de números da sequência de Fibonacci que você quer ver: '))  # noqa: E501;
    except ValueError:
        print(colored('\n\nApenas números inteiros são permitidos!\n', 'yellow'))  # noqa: E501;
    else:
        print('\n\n')
        chamar_fibonacci(quant_vezes)
        print('\n')

        resposta = input('\n\nGostaria de parar o processo [S / N]: ')
        while 'S' != resposta != 'N':
            print('\n\nUse "S" or "N" para prosseguir!')
            resposta = input('\n\nGostaria de parar o processo [S / N]: ')
            print(resposta)
            if 'S' == resposta == 'N':
                break

print('\n\nFoi um prazer!\n\n')
