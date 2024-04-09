import unittest
from dia_023.lista_duplamente_encadeada import ListaDuplamenteEncadeada


class TestandoListaComProduto(unittest.TestCase):
    def setUp(self):
        self.lista_inicial = ListaDuplamenteEncadeada()
        self.lista_inicial.adicionar_produto_a_lista_vazia('Celular')

    def testando_se_o_produto_adicionado_vira_o_primeiro_da_lista(self):
        self.lista_inicial.adicionar_produto_ao_inicio_da_lista('Fone')
        self.assertEqual('None <-> Fone <-> None <-> Celular <-> None', str(self.lista_inicial.inicio))  # noqa: E501;

    def testando_se_o_tamanho_da_lista_vira_dois_quando_um_segundo_produto_e_adicionado_a_lista(self):  # noqa: E501;
        self.lista_inicial.adicionar_produto_ao_inicio_da_lista('Fone')
        self.assertIs(len(self.lista_inicial), 2)

    def testando_se_a_cauda_da_lista_e_igual_a_sua_cabeca_apos_adicionar_um_produto_ao_inicio_da_lista(self):  # noqa: E501;
        self.lista_inicial.adicionar_produto_ao_inicio_da_lista('Fone')
        self.assertIs(self.lista_inicial.inicio, self.lista_inicial.fim)

    def testando_se_o_produto_adicionado_vira_o_ultimo_da_lista(self):
        self.lista_inicial.adicionar_produto_ao_fim_da_lista('Fone')
        self.assertEqual('None <-> Celular <-> None <-> Fone <-> None', str(self.lista_inicial.fim))  # noqa: E501;

    def testando_se_o_tamanho_da_lista_vira_dois_quando_um_produto_e_adicionado_ao_seu_fim(self):  # noqa: E501;
        self.lista_inicial.adicionar_produto_ao_fim_da_lista('Fone')
        self.assertIs(len(self.lista_inicial), 2)

    def testando_se_a_cabeca_da_lista_e_igual_ao_seu_cauda_apos_adicionar_um_produto_ao_fim_da_lista(self):  # noqa: E501;
        self.lista_inicial.adicionar_produto_ao_fim_da_lista('Fone')
        self.assertIs(self.lista_inicial.fim, self.lista_inicial.inicio)  # noqa: E501;
