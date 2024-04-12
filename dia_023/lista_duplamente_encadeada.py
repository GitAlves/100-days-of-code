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

    def __repr__(self):
        return '%s' % (self.inicio)

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

    def adicionar_produto_apos_um_certo_produto(self, produto_cadastrado, novo_produto):  # noqa: E501;
        if produto_cadastrado in str(self.inicio):
            lista_copia = self.inicio
            variavel = ListaDuplamenteEncadeada()

            while lista_copia:
                if str(lista_copia.produto) == produto_cadastrado:
                    variavel.adicionar_produto_ao_inicio_da_lista(novo_produto)
                    variavel.adicionar_produto_ao_inicio_da_lista(lista_copia.produto)  # noqa: E501;
                else:
                    variavel.adicionar_produto_ao_inicio_da_lista(lista_copia.produto)  # noqa: E501;

                lista_copia = lista_copia.anterior

            self.inicio = variavel
            self.fim = variavel
            self.tamanho += 1
        else:
            return 'Insira um produto cadastrado para poder adicionar o novo produto!'  # noqa: E501;
