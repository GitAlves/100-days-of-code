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

    def reverter_para_o_final(self):
        if self.inicio.anterior is None:
            lista_crescente = ListaDuplamenteEncadeada()
            lista_atual = self.inicio

            while lista_atual:
                lista_crescente.adicionar_produto_ao_fim_da_lista(lista_atual.produto)  # noqa: E501;
                lista_atual = lista_atual.proximo

            self.inicio = lista_crescente
            self.fim = lista_crescente
        else:
            print('A lista já está no último elemento!')

    def reverter_para_o_comeco(self):
        if self.inicio.proximo is None:
            lista_decrescente = ListaDuplamenteEncadeada()  # noqa: F841;
            lista_atual = self.inicio

            while lista_atual:
                lista_decrescente.adicionar_produto_ao_inicio_da_lista(lista_atual.produto)  # noqa: E501;
                lista_atual = lista_atual.anterior

            self.inicio = lista_decrescente
            self.fim = lista_decrescente
        else:
            print('A lista já está no primeiro elemento!')

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
            nova_lista = ListaDuplamenteEncadeada()

            while lista_copia:
                if str(lista_copia.produto) == produto_cadastrado:
                    nova_lista.adicionar_produto_ao_inicio_da_lista(novo_produto)  # noqa: E501;
                    nova_lista.adicionar_produto_ao_inicio_da_lista(lista_copia.produto)  # noqa: E501;
                else:
                    nova_lista.adicionar_produto_ao_inicio_da_lista(lista_copia.produto)  # noqa: E501;

                lista_copia = lista_copia.anterior

            self.inicio = nova_lista
            self.fim = nova_lista
            self.tamanho += 1
        else:
            return 'Insira um produto cadastrado para poder adicionar o novo produto!'  # noqa: E501;

    def adicionar_produto_antes_de_um_certo_produto(self, produto_cadastrado, novo_produto):  # noqa: E501;
        if produto_cadastrado in str(self.inicio):
            lista_copia = self.inicio
            nova_lista = ListaDuplamenteEncadeada()

            while lista_copia:
                if str(lista_copia.produto) == produto_cadastrado:
                    nova_lista.adicionar_produto_ao_inicio_da_lista(lista_copia.produto)  # noqa: E501;
                    nova_lista.adicionar_produto_ao_inicio_da_lista(novo_produto)  # noqa: E501;
                    print(nova_lista)
                else:
                    nova_lista.adicionar_produto_ao_inicio_da_lista(lista_copia.produto)  # noqa: E501;

                lista_copia = lista_copia.anterior

            self.inicio = nova_lista
            self.final = nova_lista
            self.tamanho += 1
        else:
            return 'Insira um produto cadastrado para poder adicionar o novo produto!'  # noqa: E501;

    def remover_o_ultimo_produto_da_lista(self):
        if self.tamanho > 0:
            lista_antiga = self.inicio
            nova_lista = lista_antiga.anterior
            self.inicio = nova_lista
            self.fim = nova_lista
            self.tamanho -= 1
        else:
            return 'A lista está vazia! Não há o que remover.'

    def remover_o_primeiro_elemento_da_lista(self):
        if self.tamanho > 0:
            lista_antiga = self.inicio
            nova_lista = lista_antiga.proximo
            self.inicio = nova_lista
            self.fim = nova_lista
            self.tamanho -= 1
        else:
            return 'A lista está vazia! Não há o que remover.'
