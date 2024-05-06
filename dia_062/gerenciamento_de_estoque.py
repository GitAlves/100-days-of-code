class Produto:
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade


class Node:
    def __init__(self, produto):
        self.esquerda = None
        self.direita = None
        self.produto = produto


class Raiz:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = Node(produto)
        else:
            self._inserir_recursivo(produto, self.raiz)
