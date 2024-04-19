class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.anterior = None
        self.nome = nome
        self.codigo_de_barras = codigo
        self.preco = preco
        self.quantidade = quantidade
        self.proximo = None

    def __repr__(self):
        return '%s %s' % (self.codigo_de_barras, self.nome)


class ListaDeProdutos:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def __rep__(self):
        return '%s' % (self.inicio)

    def adicionar_produto(self, nome, codigo, preco, quantidade):
        novo_produto = Produto(nome, codigo, preco, quantidade)
        if self.inicio is None:
            self.inicio = novo_produto
            self.fim = novo_produto
        else:
            self.fim.proximo = novo_produto
            novo_produto.anterior = self.fim
            self.fim = novo_produto

    def remover_produto(self, codigo):
        if self.inicio is None:
            return 'A lista está vazia! Não há o que remover'
        elif codigo in str(self.inicio):
            print('Cheguei')
            lista_copia = self.inicio
            nova_lista = ListaDeProdutos()

            while lista_copia:
                if lista_copia.codigo_de_barras == codigo:
                    print('Cheguei')
                    pass
                else:
                    nova_lista.adicionar_produto(
                        lista_copia.nome,
                        lista_copia.codigo_de_barras,
                        lista_copia.preco,
                        lista_copia.quantidade
                    )

                lista_copia = lista_copia.proximo

            nova_lista.listar_produtos()
        else:
            return 'Produto não encontrado!'

    def atualizar_quantidade(self, nome, nova_quantidade):
        if self.inicio is None:
            return 'Lista vazia! Não há produtos para serem atualizados.'
        elif nome in str(self.inicio):
            lista_copia = self.inicio
            nova_lista = ListaDeProdutos()

            while lista_copia:
                if nome == str(lista_copia.nome):
                    nova_lista.adicionar_produto(
                        lista_copia.nome,
                        lista_copia.codigo_de_barras,
                        lista_copia.preco,
                        nova_quantidade
                    )
                    print('Oi!!!')
                else:
                    nova_lista.adicionar_produto(
                        lista_copia.nome,
                        lista_copia.codigo_de_barras,
                        lista_copia.preco,
                        lista_copia.quantidade
                    )

                lista_copia = lista_copia.proximo

            nova_lista.listar_produtos()

            self.inicio = nova_lista
            self.fim = nova_lista
        else:
            return 'Esse produto não foi encontrado no estoque.'

    def listar_produtos(self):
        lista = self.inicio
        print('  Código    Produto                Preço      Quantidade\n')

        while lista:
            print(
                f'   {lista.codigo_de_barras:8} {lista.nome:22} {lista.preco} {lista.quantidade:12}\n'  # noqa: E501;
            )
            lista = lista.proximo


lista_de_produtos = ListaDeProdutos()

lista_de_produtos.adicionar_produto('Celular', '0001', 3499, 30)
lista_de_produtos.adicionar_produto('Fone Bluetooth', '0002', 249.90, 100)
lista_de_produtos.adicionar_produto('Carregador', '0003', 54.99, 50)
lista_de_produtos.adicionar_produto('Capinha', '0004', 25.99, 100)

lista_de_produtos.listar_produtos()

print(lista_de_produtos.atualizar_quantidade('Celular', 23))

lista_de_produtos.listar_produtos()

# lista_de_produtos.remover_produto('0004')

# lista_de_produtos.listar_produtos()
