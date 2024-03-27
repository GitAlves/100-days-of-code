class Produto:
    def __init__(self, produto):
        self.anterior = None
        self.produto = produto
        self.proximo = None

    def __repr__(self):
        return '%s <-> %s <-> %s' % (
            self.anterior,
            self.produto,
            self.proximo)


class ListaProdutos(Produto):
    def __init__(self):
        self.produto = None

    def __repr__(self):
        return '[' + str(self.produto) + ']'

    def inserir_produto_no_inicio(self, produto):
        if self.produto is None:
            novo_produto = Produto(produto)
            novo_produto.proximo = self.produto
            self.produto = novo_produto
        else:
            novo_produto = Produto(produto)
            lista_produtos = self.produto
            novo_produto.proximo = lista_produtos
            self.produto = novo_produto
            print(novo_produto)
            print(lista_produtos)
