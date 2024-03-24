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
        self.pacientes_inseridos = list()

    def __repr__(self):
        return '[' + str(self.paciente) + ']'

    def adicionar_paciente(self, paciente=None):
        try:
            print(int(paciente))
        except TypeError:
            '''
            Caso nenhum nome tenha sido passado
            '''
            return print('Por favor, insira o nome paciente.')
        except ValueError:
            '''
            Se um nome ter sido passado
            '''
            self.pacientes_inseridos.append(paciente)
            novoPaciente = UmPaciente(paciente)
            novoPaciente.proximoPaciente = self.paciente
            self.paciente = novoPaciente
        else:
            '''
            Se um nome ter sido passado para o método
            '''
            return print('O paciente deve ter um nome com letras, não números!')  # noqa: E501;

        print(f'\nAdicionando {paciente} a fila!\n')

    def adicionar_paciente_no_fim(self, paciente=None):
        try:
            teste_tipo = int(paciente)  # noqa: F841;
        except TypeError:
            '''
            Caso nenhum nome tenha sido passado para o método
            '''
            return print('Insira o nome do paciente para continuar!')
        except ValueError:
            '''
            Significa que um nome foi passado para o método
            '''
            self.pacientes_inseridos.append(paciente)
            lista = self.paciente
            novo_paciente = UmPaciente(paciente)

            while lista.paciente is not None:
                if lista.proximoPaciente is None:
                    lista.proximoPaciente = novo_paciente
                    break

                lista = lista.proximoPaciente
        else:
            return print('O nome do paciente deve ter letras, não números')

        print(f'\nPaciente "{paciente}" adicionado no início da fila!\n')

    def remover_paciente(self, paciente=None):
        try:
            teste_tipo = int(paciente)  # noqa: F841;
        except TypeError:
            return print('Para remover um paciente da fila, é necessário inserir o seu nome!')  # noqa: E501;
        except ValueError:
            try:
                if paciente in self.pacientes_inseridos:
                    lista_apoio = self.paciente

                    if lista_apoio.paciente == paciente:
                        self.paciente = lista_apoio.proximoPaciente
                    else:
                        auxiliar = None
                        while lista_apoio.paciente != paciente:
                            if lista_apoio.proximoPaciente.paciente == paciente:  # noqa: E501;
                                auxiliar = lista_apoio.proximoPaciente
                                lista_apoio.proximoPaciente = auxiliar.proximoPaciente  # noqa: E501;
                                break

                            lista_apoio = lista_apoio.proximoPaciente
                else:
                    return print('Este paciente não foi listado!')
            except AttributeError:
                return print('Não há como remover pacientes da lista, pois ela está vazia!')  # noqa: E501;
            else:
                print(f'\nPaciente "{paciente}" deixou a fila!\n')
        else:
            print('O nome do paciente não pode ser um número!')

    def listar_pacientes(self):
        lista = []
        lista_apoio = self.paciente
        try:
            while lista_apoio.paciente is not None:
                lista.append(lista_apoio.paciente)
                if lista_apoio.proximoPaciente is None:
                    break

                lista_apoio = lista_apoio.proximoPaciente
        except AttributeError:
            return print('Não há pacientes para serem mostrados.')
        else:
            lista.reverse()

            posicao, nome = 'Posição', 'Nome'
            print('--------------------------------')
            print('       LISTANDO PACIENTES      ')
            print('--------------------------------\n')

            sleep(2)

            print(f'{posicao:20} {nome}\n')

            for indice, paciente, estado in enumerate(lista):
                print(f'   {indice + 1}                {paciente}')
