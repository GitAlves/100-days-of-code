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
            tipo_dado = int(paciente)  # noqa: F841;
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
        if len(self.pacientes_inseridos) > 0:
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
        else:
            print('A lista está vazia. Não há porque passar pacientes na frente.')  # noqa: E501;

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


lista_pacientes = ListaPacientes()

print('\n\n--- Caso 1: Removendo pacientes ---\n\n')
sleep(2)
print('Tentando remover um paciente sem dizer qual\n')
sleep(2)
print('Resultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.remover_paciente()

sleep(1)
print('\n\nTentando remover um paciente que ainda não foi adicionado\n')
sleep(2)
print('Resultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.remover_paciente('Joaquim')

sleep(2)
print('\n\nPassando um número como nome de paciente\n')
sleep(2)
print('Resultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.remover_paciente(3)

sleep(1)
print('\n\n--- Caso 2: Adicionando pacientes ao fim da lista ---')
sleep(2)
print('\n\nQuando se tenta adicionar pacientes ao fim da lista, sendo que ela está vazia\n')  # noqa: E501;
print('Resultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.adicionar_paciente_no_fim('Joaquim')

sleep(1)
print('\n\nTentando adicionar pacientes ao fim da lista, sem passar o paciente')  # noqa: E501;
sleep(2)
print('Adicionando o primeiro paciente da lista: ', end='')
lista_pacientes.adicionar_paciente('Joanna')
sleep(2)
print('\nAdicionando um novo paciente, sem adicionar o paciente')
print('\nResultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.adicionar_paciente_no_fim()

sleep(1)
print('\n\nAdicionando um número como paciente\n')
sleep(2)
print('Resultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.adicionar_paciente_no_fim(3)

sleep(1)
print('\n\n--- Caso 3: Listando pacientes ---')
sleep(2)
print('Removendo o único paciente da lista: ', end='')
sleep(2)
lista_pacientes.remover_paciente('Joanna')

sleep(1)
print('Listando uma lista vazia')
print('Resultado do tratamento de erro: ', end='')
sleep(2)
lista_pacientes.listar_pacientes()

sleep(1)
print('\n\n--- Caso 4: Adicionado pacientes ---\n')
sleep(2)
print('Adicionado pacientes, sem digitar o nome do paciente\n')
print('Resultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.adicionar_paciente()

sleep(1)
print('\n\nInserindo um número como nome do paciente\n')
sleep(2)
print('Resultado do tratamento do erro: ', end='')
sleep(2)
lista_pacientes.adicionar_paciente(3)
print('\n\n')
