class Livro:
    def __init__(self, titulo, num_paginas):
        self._titulo = titulo
        self._num_paginas = num_paginas
        self._titulo_anterior = None

    def __repr__(self):
        return '%s, %s ->  %s' % (self._titulo, self._num_paginas, self._titulo_anterior)


class PilhaDeLivros:
    def __init__(self):
        self._livro_atual = None

    def __repr__(self):
        return '%s' % (self._livro_atual)

    def adicionar_livro(self, livro, num_paginas):
        novo_livro = Livro(livro, num_paginas)
        if self._livro_atual is None:
            self._livro_atual = novo_livro
        else:
            pilha = self._livro_atual
            novo_livro._titulo_anterior = pilha
            self._livro_atual = novo_livro
