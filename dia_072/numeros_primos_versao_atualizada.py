def numero_primo(numero):
    quant_divisores = list(
        filter(
            lambda divisor: numero % divisor == 0,
            list(
                range(1, numero + 1)
            )
        )
    )

    return f'\n{numero} é um número primo!' if len(quant_divisores) == 0 else f'\n{numero} não é um número primo!'  # noqa: E501;


resposta = 'N'
while resposta != 'S':

    numero = numero_primo(
        int(input('\n\nDigite um número qualquer: ')))

    print(numero)

    resposta = input('\nGostaria de sair [S/N]: ')

print('\n\nFoi um prazer!!!\n\n')
