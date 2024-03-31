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

    quantidade_itens = 0

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
        resultado += ' <-> None ]'
        return resultado
    
    def __len__(self):
        return self.quantidade_itens

    def inserir_produto_no_inicio(self, produto):
        novo_produto = Produto(produto)
        if self.anterior is None:
            self.anterior = novo_produto
            self.proximo = novo_produto
            self.quantidade_itens += 1
        else:
            novo_produto.proximo = self.anterior
            self.anterior.anterior = novo_produto
            novo_produto.anterior = None
            self.anterior = novo_produto
            self.quantidade_itens += 1

        print(f'\nProduto "{produto}" foi adicionado com sucesso ao início da lista!\n')  # noqa: E501;

    def inserir_produto_no_final(self, produto):
        novo_produto = Produto(produto)
        if self.anterior is None:
            self.anterior = novo_produto
            self.proximo = novo_produto
            self.quantidade_itens += 1
        else:
            self.proximo.proximo = novo_produto
            novo_produto.anterior = self.proximo
            self.proximo = novo_produto
            self.quantidade_itens += 1

        print(f'\nProduto "{produto}" foi adicionado com sucesso ao fim da lista!\n')  # noqa: E501;
