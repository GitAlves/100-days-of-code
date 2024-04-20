import unittest
from dia_023_a_048.lista_duplamente_encadeada import Produto


class TestandoNoDuplo(unittest.TestCase):
    def setUp(self):
        self.elemento_duplo = Produto('Celular')

    def testando_insercao_de_produto(self):
        self.assertEqual(self.elemento_duplo.produto, 'Celular')

    def testando_se_a_lista_criada_e_a_correta(self):
        self.assertEqual(str(self.elemento_duplo), 'None <-> Celular <-> None')
