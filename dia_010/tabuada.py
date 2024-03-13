def tabuada(numero, multiplicadores=10):
    for multiplicador in range(1, multiplicadores + 1):
        print(f'{numero} X {multiplicador} = {numero * multiplicador}')


numero_escolhido = int(input('Insira um número para ver a sua tabuada: '))
quantidade = int(input(
    'Insira até onde você quer saber sobre a tabuada do número: ')
    )

print('\nIniciando tabuada...\n')

tabuada(numero_escolhido, quantidade)

print('\nProcesso finalizado!')
