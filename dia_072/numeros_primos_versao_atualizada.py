def numero_primo(numero):
    if numero <= 1:
        return False

    quant_divisores = list(
        filter(
            lambda divisor: numero % divisor == 0,
            list(range(1, numero + 1))
        )
    )

    return True if len(quant_divisores) == 2 else False  # noqa: E501;


resposta = 'N'
while resposta != 'S':

    numero = numero_primo(
        int(input('\n\nDigite um número qualquer: ')))

    print(numero)

    resposta = input('\nGostaria de sair [S/N]: ')

print('\n\nFoi um prazer!!!\n\n')
