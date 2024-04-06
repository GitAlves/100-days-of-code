class Produto:
    def __init__(self, produto):
        self.anterior = None
        self.produto = produto
        self.proximo = None

    def __repr__(self):
        return '%s <-> %s <-> %s' % (
            self.anterior,
            self.produto,
            self.proximo
        )


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar_produto_a_lista_vazia(self, produto):
        novo_produto = Produto(produto)
        self.inicio = novo_produto
        self.fim = novo_produto
        self.tamanho += 1
