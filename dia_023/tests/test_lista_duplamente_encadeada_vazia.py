import unittest
from dia_023.lista_duplamente_encadeada import ListaDuplamenteEncadeada


class TestandoListaDuplamenteEncadeada(unittest.TestCase):
    def setUp(self):
        self.lista_inicial = ListaDuplamenteEncadeada()

    def testando_se_a_lista_possui_um_inicio_com_valor_nulo_ao_ser_criada(self):  # noqa: E501;
        self.assertEqual(self.lista_inicial.inicio, None)

    def testando_se_a_lista_possui_um_final_com_valor_nulo_quando_criada(self):
        self.assertEqual(self.lista_inicial.fim, None)

    def testando_se_o_tamanho_da_lista_e_zero_quando_criada(self):
        self.assertEqual(len(self.lista_inicial), 0)

    def testando_se_o_produto_esta_sendo_adicionado_a_lista_vazia(self):
        self.lista_inicial.adicionar_produto_a_lista_vazia('Celular')
        self.assertEqual(self.lista_inicial.inicio.produto, 'Celular')

    def testando_se_o_tamanho_da_lista_vira_um_ao_se_adicionar_o_primeiro_produto(self):  # noqa: E501;
        self.lista_inicial.adicionar_produto_a_lista_vazia('Celular')
        self.assertEqual(self.lista_inicial.tamanho, 1)

    def testando_a_estrutura_da_lista_quando_um_produto_e_adicionado(self):
        self.lista_inicial.adicionar_produto_a_lista_vazia('Celular')
        self.assertEqual(str(self.lista_inicial.inicio), 'None <-> Celular <-> None')  # noqa: E501;

    def testando_se_a_cabeca_da_lista_e_igual_a_sua_calda(self):
        self.lista_inicial.adicionar_produto_a_lista_vazia('Celular')
        self.assertIs(self.lista_inicial.inicio, self.lista_inicial.fim)

    def testando_se_ao_adicionar_um_produto_no_inicio_da_lista_vazia_este_se_torna_o_primeiro_produto(self):  # noqa: E501;
        self.lista_inicial.adicionar_produto_ao_inicio_da_lista('Celular')
        self.assertEqual(str(self.lista_inicial.inicio), 'None <-> Celular <-> None')  # noqa: E501;
