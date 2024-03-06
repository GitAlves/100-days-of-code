def impar_ou_par(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par!'
    else:
        return f'O número {numero} é ímpar!'


sair = 'n'
while sair != 'y':
    num_inteiro = int(input('Digite um número: '))

    print(impar_ou_par(num_inteiro))

    sair = input('Gostaria de encerrar o programa [y/n]: ')

print('Foi um prazer!')
