import unittest
from dia_023_a_042.lista_duplamente_encadeada import ListaDuplamenteEncadeada


class TestandoARemocaoDeItensDaListaDupla(unittest.TestCase):
    def setUp(self):
        self.lista_inicial = ListaDuplamenteEncadeada()
        self.lista_inicial.adicionar_produto_a_lista_vazia('Celular')
        self.lista_inicial.adicionar_produto_ao_inicio_da_lista('Fone')
        self.lista_inicial.adicionar_produto_ao_fim_da_lista('Carregador')

    def testando_se_o_ultimo_produto_esta_sendo_removido(self):
        self.lista_inicial.remover_o_ultimo_produto_da_lista()
        self.assertEqual(
            str(self.lista_inicial),
            'None <-> Fone <-> None <-> Celular <-> None'
        )

    def testando_se_a_mensagem_aparece_quando_se_tenta_excluir_o_ultimo_item_de_uma_lista_vazia(self):  # noqa: E501;
        outra_lista = ListaDuplamenteEncadeada()
        mensagem = outra_lista.remover_o_ultimo_produto_da_lista()
        self.assertEqual(mensagem, 'A lista está vazia! Não há o que remover.')

    def testando_se_o_tamanho_da_lista_diminui_quando_o_ultimo_item_e_removido(self):  # noqa: E501;
        self.lista_inicial.remover_o_ultimo_produto_da_lista()
        self.assertEqual(len(self.lista_inicial), 2)
