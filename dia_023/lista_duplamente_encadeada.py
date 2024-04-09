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

    def adicionar_produto_ao_inicio_da_lista(self, produto):
        if self.tamanho == 0:
            return self.adicionar_produto_a_lista_vazia(produto)
        else:
            novo_no = Produto(produto)
            novo_no.proximo = self.inicio
            novo_no.anterior = None
            self.inicio = novo_no
            self.fim = novo_no
            self.tamanho += 1

    def adicionar_produto_ao_fim_da_lista(self, produto):
        if self.tamanho == 0:
            return self.adicionar_produto_a_lista_vazia(produto)
        else:
            novo_no = Produto(produto)
            novo_no.anterior = self.fim
            novo_no.proximo = None
            self.fim = novo_no
            self.inicio = novo_no
            self.tamanho += 1
