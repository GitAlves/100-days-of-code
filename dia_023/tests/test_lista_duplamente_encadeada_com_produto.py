import unittest
from dia_023.lista_duplamente_encadeada import ListaDuplamenteEncadeada


class TestandoListaComProduto(unittest.TestCase):
    def setUp(self):
        lista_inicial = ListaDuplamenteEncadeada()
        lista_inicial.adicionar_produto_a_lista_vazia('Celular')

    def testando_
