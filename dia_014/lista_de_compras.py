class ListaDeCompras:
    def __init__(self):
        self.__itens = []
        self.__quantidade = []

    def inserir_itens(self, item, quantidade):
        self.__itens.append(item)
        self.__quantidade.append(quantidade)

    def remover_item(self, item):
        if item in self.__itens:
            posicao = self.__itens.index(item)

            del self.__itens[posicao]
            del self.__quantidade[posicao]

<<<<<<< HEAD
            print(f'\nItem "{item}" removido da lista de compras.\n')
=======
            print(f'\nItem {item} removido da lista de compras.\n')
>>>>>>> 7a096fd4722732d439d660a7fc8bd46896a17361

    def listar_itens(self):
        print('    Item         Quantidade     ', end='\n\n')
        for posicao, item in enumerate(self.__itens):
            print(f'{posicao + 1} - {self.__itens[posicao]:20} {self.__quantidade[posicao]}')  # noqa: E501;


lista_compras = ListaDeCompras()
lista_compras.inserir_itens('Feijão', 3)
lista_compras.inserir_itens('Arroz', 2)
lista_compras.inserir_itens('Ruffles', 10)
lista_compras.listar_itens()
lista_compras.remover_item('Arroz')
lista_compras.listar_itens()
