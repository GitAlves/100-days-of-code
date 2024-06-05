def tamanho_tabuada():
    while True:
        try:
            quantidade = range(
                0, int(
                    input(
                        '\nInsira até onde você quer saber da tabuada do número: '  # noqa: E501;
                    )
                ) + 1
            )
        except ValueError:
            print('\n\nUse um número inteiro para escolher o tamanho da tabuada!')  # noqa: E501;
        else:
            return quantidade


escolha = 'N'
while escolha != 'S':
    try:
        numero_escolhido = int(input('\n\nInsira um número para ver a sua tabuada: '))  # noqa: E501;
    except ValueError:
        print('\n\nInsira um número inteiro para continuar!')
    else:
        quantidade = tamanho_tabuada()

        tabuada = list(map(lambda x: (numero_escolhido, x, x * numero_escolhido), quantidade))  # noqa: E501;

        print('\n\n')
        for elemento in tabuada:
            print(f'{elemento[0]} x {elemento[1]} = {elemento[2]}')

        while True:
            escolha = input('\n\nGostaria de sair [S/N]: ')

            match escolha:
                case 'S':
                    break
                case 'N':
                    break
                case _:
                    print('\n\nDigite [S] para sair ou [N] para continuar vendo tabuadas!')  # noqa: E501;


print('\n\nFoi um prazer!\n\n')
