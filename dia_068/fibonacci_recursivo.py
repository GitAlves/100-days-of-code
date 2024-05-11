def chamar_fibonacci(vezes, anterior=0, atual=1):
    print(atual, end=' ')

    atual = atual + anterior
    anterior = atual - anterior
    vezes -= 1

    if vezes > 0:
        chamar_fibonacci(vezes, anterior, atual)


resposta = 'N'
while resposta != 'S':
    quant_vezes = int(input('\n\nDigite a quantidade de números da sequência de Fibonacci que você quer ver: '))  # noqa: E501;

    print('\n\n')
    chamar_fibonacci(quant_vezes)
    print('\n')

    resposta = input('\n\nGostaria de parar o processo [S / N]: ')


print('\n\nFoi um prazer!\n\n')
