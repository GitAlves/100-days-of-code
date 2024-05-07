class Produto:
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade


class Node:
    def __init__(self, produto):
        self.esquerdo = None
        self.direito = None
        self.produto = produto


class Raiz:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = Node(produto)
        else:
            self._inserir_recursivo(produto, self.raiz)

    def _inserir_recursivo(self, produto, no):
        if produto.id < no.produto.id:
            if no.esquerdo is None:
                no.esquerdo = Node(produto)
            else:
                self._inserir_recursivo(produto, no.esquerdo)
        elif produto.id > no.produto.id:
            if no.direito is None:
                no.direito = Node(produto)
            else:
                self._inserir_recursivo(produto, no.direito)
        else:
            '''
            Significa que o ID do novo produto já existe no sistema.
            Assim, os dados desse novo produto irão substituir os
            do produto antigo que possuía o mesmo ID.
            '''
            no.produto = produto.nome
            no.quantidade = produto.quantidade


produto1 = Produto(1, 'Ruffles', 50)
produto2 = Produto(0, 'Pringles', 43)
produto3 = Produto(2, 'Fandangos', 38)
produto4 = Produto(1, 'Ruffles', 52)

arvore = Raiz()
arvore.inserir(produto1)
arvore.inserir(produto2)
arvore.inserir(produto3)
arvore.inserir(produto4)
