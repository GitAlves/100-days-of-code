escolha = 'N'
while escolha != 'S':
    numero_escolhido = int(input('\n\nInsira um número para ver a sua tabuada: '))  # noqa: E501;
    quantidade = range(
        0, int(
            input(
                '\nInsira até onde você quer saber da tabuada do número: '
            )
        )
    )

    lista_numeros = list(map(lambda x: (numero_escolhido, x, x * numero_escolhido), quantidade))  # noqa: E501;

    print(lista_numeros)

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
