from time import sleep


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


lista_encadeada = ListaPacientes()
while True:
    nome_paciente = input('\nDigite o nome do paciente: ')

    if nome_paciente != '':
        lista_encadeada.adicionar_paciente(nome_paciente)
        sleep(2)

        print('\n--------- Listando pacientes -----------\n')
        print(lista_encadeada)
    else:
        break

print('\n\n------- PROCESSO ENCERRADO --------\n\n')
sleep(2)
print(f'\nA lista final foi: {lista_encadeada}\n')
