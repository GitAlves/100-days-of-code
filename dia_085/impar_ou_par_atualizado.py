def impar_ou_par(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par!'
    else:
        return f'O número {numero} é impar!'


sair = 'n'
while sair != 'y':
    try:
        num_inteiro = int(input('Digite um número: '))
    except ValueError:
        print('Insira um número inteiro para ser testado!')
    else:
        print(impar_ou_par(num_inteiro))

        while True:
            sair = input('Gostaria de encerrar o programa [y/n]: ')

            match sair:
                case 'y':
                    sair = 'y'
                    break
                case 'n':
                    sair = 'n'
                    break
                case _:
                    print('Digite [y] para sair ou [n] para continuar!')

print('Foi um prazer!')
