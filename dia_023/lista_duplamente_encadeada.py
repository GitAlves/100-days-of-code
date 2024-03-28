from time import sleep


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
            self.produto = novo_produto
        else:
            novo_produto = Produto(produto)
            novo_produto.proximo = self.produto
            self.produto = novo_produto

        print(f'\nProduto "{produto}" foi adicionado com sucesso!\n')


lista_produtos = ListaProdutos()
print('\nInserindo "celular" como o primeiro produto na lista: \n')
sleep(2)
lista_produtos.inserir_produto_no_inicio('Celular')
sleep(2)
print('\nInserindo "Fone de ouvido " como o segundo produto da lista: \n')
sleep(2)
lista_produtos.inserir_produto_no_inicio('Fone bluetooth')
sleep(2)
print(f'Por hora, a lista duplamente encadeada está ficando assim: \n\n{lista_produtos}\n\n')  # noqa: E501;
