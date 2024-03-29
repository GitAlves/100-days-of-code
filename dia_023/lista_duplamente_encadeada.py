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


class ListaProdutos:
    def __init__(self):
        self.anterior = None
        self.proximo = None

    def __repr__(self):
        if self.anterior is None:
            return '[]'

        iterador = self.anterior
        resultado = '[ None <-> '
        while iterador:
            resultado += iterador.produto
            if iterador.proximo:
                resultado += ' <-> '
            iterador = iterador.proximo
        resultado += ' <-> None]'
        return resultado

    def inserir_produto_no_inicio(self, produto):
        novo_produto = Produto(produto)
        if self.anterior is None:
            self.anterior = novo_produto
            self.proximo = novo_produto
        else:
            novo_produto.proximo = self.anterior
            self.anterior.anterior = novo_produto
            novo_produto.anterior = None
            self.anterior = novo_produto

        print(f'\nProduto "{produto}" foi adicionado com sucesso!\n')

    def inserir_produto_no_final(self, produto):
        novo_produto = Produto(produto)
        if self.anterior is None:
            self.anterior = novo_produto
            self.proximo = novo_produto
        else:
            self.proximo.proximo = novo_produto
            novo_produto.anterior = self.proximo
            self.ultimo = novo_produto

        print(f'\nProduto "{produto}" adicionado com sucesso!\n')
