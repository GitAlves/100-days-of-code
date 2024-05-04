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
