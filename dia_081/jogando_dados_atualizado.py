from random import randint


class Dado:
    def __init__(self, lados):
        self._lados = lados

    def modificar_quantidade_lados(self, nova_quantidade):
        print('\n\nNovo dado criado com sucesso!')
        self._lados = nova_quantidade

    @property
    def sortear_lado(self):
        return randint(0, self._lados)


dado_exemplo = Dado(20)

resp = 'N'
while resp != 'S':
    try:
        resp = int(input(
            '\n\nDigite [1] para sortear um lado do dado.\n'
            'Digite [2] para modificar a quantidade de dados do lado.\n'
            'Digite [3] para encerrar o programa.\n'
            'Digite a sua escolha: '
            )
        )
    except ValueError:
        print('\n\nUse números inteiros para prosseguir com o uso do projeto!')  # noqa: E501;
    else:
        match resp:
            case 1:
                print(f'\n\nNúmero sorteado: {dado_exemplo.sortear_lado}')
            case 2:
                while 2 != 'dois':
                    try:
                        nova_quantidade = int(
                            input(
                                '\n\nDigite quantos lados o novo dado terá: '
                            )
                        )
                    except ValueError:
                        print('\n\nInsira um número inteiro para modificar a quantidade de lados do dado!')  # noqa: E501;
                    else:
                        dado_exemplo.modificar_quantidade_lados(nova_quantidade)  # noqa: E501;
                        break
            case 3:
                resp = 'S'
            case _:
                print('Use 1, 2 ou três para prosseguir com o uso do projeto!')

print('\n\nAté mais!\n\n')
