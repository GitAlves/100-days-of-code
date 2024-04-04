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
