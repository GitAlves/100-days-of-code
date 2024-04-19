import unittest
from dia_023_a_042.lista_duplamente_encadeada import ListaDuplamenteEncadeada


class TestandoReversaoDaPosicaoDoPonteiroDaLista(unittest.TestCase):
    def setUp(self):
        self.lista_base = ListaDuplamenteEncadeada()
        self.lista_base.adicionar_produto_a_lista_vazia('Celular')

    def testando_se_o_item_anterior_e_none_quando_se_reverte_a_lista_para_o_comeco(self):  # noqa: E501;
        self.lista_base.adicionar_produto_ao_fim_da_lista('Carregador')
        self.lista_base.reverter_para_o_comeco()

        self.assertEqual(self.lista_base.produto.anterior, None)

    def testando_a_mensagem_quando_a_lista_e_revertida_para_o_comeco(self):
        self.lista_base.adicionar_produto_ao_inicio_da_lista('Fone')
        mensagem = self.lista_base.reverter_para_o_comeco()

        self.assertEqual(mensagem, 'A lista já está no começo!')

    def testando_se_o_proximo_item_e_none_quando_se_reverte_a_lista_para_o_final(self):  # noqa: E501;
        self.lista_base.adicionar_produto_ao_inicio_da_lista('Fone')
        self.lista_base.reverter_para_o_final()

        self.assertEqual(self.lista_base.inicio.proximo, None)

    def testando_a_mensagem_quando_a_lista_e_revertida_para_o_final(self):
        self.lista_base.adicionar_produto_ao_fim_da_lista('Carregador')
        mensagem = self.lista_base.reverter_para_o_final()

        self.assertEqual(mensagem, 'A lista já está no final!')
