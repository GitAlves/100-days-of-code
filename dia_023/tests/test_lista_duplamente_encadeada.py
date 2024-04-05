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
