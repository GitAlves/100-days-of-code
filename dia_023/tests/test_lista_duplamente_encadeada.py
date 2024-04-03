import unittest
from dia_023.lista_duplamente_encadeada import Produto


class TestandoNoDuplo(unittest.TestCase):
    def setUp(self):
        self.no_unico = Produto('Celular')

    def testando_insercao_de_produto(self):
        self.assertEqual(self.no_unico, 'Celular')

    def testando_se_a_lista_criada_e_correta(self):
        self.assertEqual(print(self.no_unico), 'None <-> Celular <-> None')
