class Livro:
    def __init__(self, titulo, num_paginas):
        self._titulo = titulo
        self._num_paginas = num_paginas
        self._titulo_anterior = None

    def __repr__(self):
        return '%s, %s ->  %s' % (
            self._titulo,
            self._num_paginas,
            self._titulo_anterior)


class PilhaDeLivros:
    def __init__(self):
        self._livro_atual = None

    def __repr__(self):
        return '%s, %s -> %s' % (
            self._livro_atual._titulo,
            self._livro_atual._num_paginas,
            self._livro_atual._titulo_anterior)

    def adicionar_livro(self, livro, num_paginas):
        novo_livro = Livro(livro, num_paginas)
        if self._livro_atual is None:
            self._livro_atual = novo_livro
        else:
            pilha = self._livro_atual
            novo_livro._titulo_anterior = pilha
            self._livro_atual = novo_livro

    def remover_livro(self):
        if self._livro_atual is None:
            print('A pilha está vazia! Não há o que remover.')
        else:
            pilha = self._livro_atual
            self._livro_atual = pilha._titulo_anterior

    def mostrar_ultimo_livro(self):
        pilha = self._livro_atual
        print(f'Livro: {pilha._titulo} \nNúmero de páginas: {pilha._num_paginas}\n')  # noqa: E501;

    def mostrar_livros(self):
        print('Título               Nº de páginas\n')

        pilha = self._livro_atual
        while pilha:
            if pilha._titulo_anterior is None:
                print(f'{pilha._titulo:25} {pilha._num_paginas} <- Base da pilha')  # noqa: E501;
                break
            print(f'{pilha._titulo:25} {pilha._num_paginas}')

            pilha = pilha._titulo_anterior
