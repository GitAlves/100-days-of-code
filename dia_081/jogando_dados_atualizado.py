from random import randint


class Dado:
    def __init__(self, lados):
        self._lados = lados

    def modificar_quantidade_lados(self, nova_quantidade):
        self._lados = nova_quantidade

    def sortear_lado(self):
        return randint(0, self._lados)


dado_exemplo = Dado(20)

resp = 'N'
while resp != 'S':
    print(f'\n\nNúmero sorteado: {dado_exemplo.sortear_lado()}\n\n')

    resp = input('Gostaria de encerrar o programa [S/N]: ')

print('\n\nAté mais!\n\n')
