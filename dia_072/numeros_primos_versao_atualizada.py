def numero_primo(numero):
    lista_divisores = [numero for numero in range(1, numero + 1)]
    quant_divisores = [
        divisor for divisor in lista_divisores if numero % divisor == 0  # noqa: E501;
        ]

    if len(quant_divisores) == 2:
        return f'\n{numero} é um número primo! \nLista divisores: {quant_divisores}\n'  # noqa: E501;
    else:
        return f'\n{numero} não é um número primo. \nLista divisores: {quant_divisores}\n'  # noqa: E501;


resposta = 'N'
while resposta != 'S':

    numero = numero_primo(
        int(input('\n\nDigite um número qualquer: ')))

    print(numero)

    resposta = input('\nGostaria de sair [S/N]: ')

print('\n\nFoi um prazer!!!\n\n')
