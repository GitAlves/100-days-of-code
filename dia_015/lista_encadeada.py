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
        ...

    def remover_paciente(self, paciente):
        lista_apoio = self.paciente

        if lista_apoio.paciente == paciente:
            self.paciente = lista_apoio.proximoPaciente

        print(f'\nPaciente {paciente} removido da fila!\n')
