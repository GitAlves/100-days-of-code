class UmPaciente:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximoPaciente = None

    def __repr__(self):
        return '%s -> %s' % (self.paciente, self.proximoPaciente)


class ListaPacientes(UmPaciente):
    def __init__(self):
        self.paciente = None

    def __repr__(self):
        return '[' + str(self.paciente) + ']'

    def adicionar_paciente(self, paciente):
        novoPaciente = UmPaciente(paciente)
        novoPaciente.proximoPaciente = self.paciente
        self.paciente = novoPaciente

        print(f'\nAdicionando {paciente} a fila!\n')

    def adicionar_paciente_no_fim(self, paciente):
        lista = self.paciente
        novo_paciente = UmPaciente(paciente)

        while lista.paciente is not None:
            if lista.proximoPaciente is None:
                lista.proximoPaciente = novo_paciente
                break

            lista = lista.proximoPaciente

        print(f'\nPaciente "{paciente}" adicionado no início da fila!\n')

    def remover_paciente(self, paciente):
        lista_apoio = self.paciente

        if lista_apoio.paciente == paciente:
            self.paciente = lista_apoio.proximoPaciente
        else:
            auxiliar = None
            while lista_apoio.paciente != paciente:
                if lista_apoio.proximoPaciente.paciente == paciente:
                    auxiliar = lista_apoio.proximoPaciente
                    lista_apoio.proximoPaciente = auxiliar.proximoPaciente
                    break

                lista_apoio = lista_apoio.proximoPaciente

        print(f'\nPaciente "{paciente}" removido da fila!\n')

    def listar_pacientes(self):
        lista = []
        lista_apoio = self.paciente

        while lista_apoio.paciente is not None:
            lista.append(lista_apoio.paciente)
            if lista_apoio.proximoPaciente is None:
                break

            lista_apoio = lista_apoio.proximoPaciente

        lista.reverse()

        posicao, nome = 'Posição', 'Nome'
        print('--------------------------------')
        print('         LISTANDO PACIENTES      ')
        print('--------------------------------\n')

        print(f'{posicao:20} {nome}\n')

        for indice, paciente in enumerate(lista):
            print(f'   {indice}                {paciente}')
