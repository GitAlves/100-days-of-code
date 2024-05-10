class Produto:
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade

    def __repr__(self):
        return ' %s %s %s ' % (
            self.id,
            self.nome,
            self.quantidade
        )


class Node:
    def __init__(self, produto):
        self.esquerdo = None
        self.direito = None
        self.produto = produto


class Raiz:
    def __init__(self):
        self.raiz = None

    def __repr__(self):
        return self._representar_recursivo(self.raiz)

    def _representar_recursivo(self, no):
        if no is None:
            pass
        else:
            representar = ''
            representar += str((self._representar_recursivo(no.esquerdo)))
            representar += str(no.produto) + '\n'
            representar += str(self._representar_recursivo(no.direito))
            return representar

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = Node(produto)
        else:
            self._inserir_recursivo(produto, self.raiz)

    def _inserir_recursivo(self, produto, no):
        if produto.id < no.produto.id:
            if no.esquerdo is None:
                no.esquerdo = Node(produto)
            else:
                self._inserir_recursivo(produto, no.esquerdo)
        elif produto.id > no.produto.id:
            if no.direito is None:
                no.direito = Node(produto)
            else:
                self._inserir_recursivo(produto, no.direito)
        else:
            '''
            Significa que o ID do novo produto já existe no sistema.
            Assim, os dados desse novo produto irão substituir os
            do produto antigo que possuía o mesmo ID.
            '''
            no.produto.nome = produto.nome
            no.produto.quantidade = produto.quantidade

    def buscar_item(self, codigo):
        if self.raiz is None:
            print('A árvore está vazia! Não há o que mostrar.')
        else:
            return self._buscar_item_recursivo(codigo, self.raiz)

    def _buscar_item_recursivo(self, codigo, no):
        if no is None or no.produto.id == codigo:
            print(f'ID {codigo}: "{no.produto.nome}" - com {no.produto.quantidade} unidades - encontrado com sucesso!')  # noqa: E501;
        elif codigo < no.produto.id:
            self._buscar_item_recursivo(codigo, no.esquerdo)
        elif codigo > no.produto.id:
            self._buscar_item_recursivo(codigo, no.direito)


produto1 = Produto(1, 'Ruffles', 50)
produto2 = Produto(0, 'Pringles', 43)
produto3 = Produto(2, 'Fandangos', 38)
produto4 = Produto(1, 'Ruffles', 41)
produto5 = Produto(3, 'Cheetos', 23)
produto6 = Produto(48, 'Lobitos', 67)
produto7 = Produto(4, 'Torcida', 56)

arvore = Raiz()
arvore.inserir(produto1)
arvore.inserir(produto2)
arvore.inserir(produto3)
arvore.inserir(produto4)
arvore.inserir(produto5)
arvore.inserir(produto6)
arvore.inserir(produto7)

print('\n\nCódigo   Nome   Quantidade\n')
print(arvore)
print('\n\n')
