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


class ListaProdutos:
    def __init__(self):
        self.anterior = None
        self.proximo = None
        self.tamanho = 0

    def vazia(self):
        if self.tamanho == 0:
            return True
        return False

    # def __repr__(self):
    #     return '[' + str(self.produto) + ']'

    def inserir_produto_no_inicio(self, produto):
        novo_produto = Produto(produto)
        if self.vazia():
            self.anterior = novo_produto
            self.proximo = novo_produto
        else:
            novo_produto.proximo = self.anterior
            self.anterior.anterior = novo_produto
            novo_produto.anterior = None
            self.anterior = novo_produto
        self.tamanho += 1

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
print(lista_produtos.anterior)
print(lista_produtos.proximo)
