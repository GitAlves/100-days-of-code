def impar_ou_par(numero):
    if numero % 2 == 0:
        return f'\n\nO número {numero} é par!'
    else:
        return f'\n\nO número {numero} é impar!'


sair = 'n'
while sair != 'y':
    try:
        num_inteiro = int(input('\n\nDigite um número: '))
    except ValueError:
        print('\n\nInsira um número inteiro para ser testado!')
    else:
        print(impar_ou_par(num_inteiro))

        while True:
            sair = input('\n\nGostaria de encerrar o programa [y/n]: ')

            match sair:
                case 'y':
                    sair = 'y'
                    break
                case 'n':
                    sair = 'n'
                    break
                case _:
                    print('\n\nDigite [y] para sair ou [n] para continuar!')

print('\n\nFoi um prazer!\n\n')
