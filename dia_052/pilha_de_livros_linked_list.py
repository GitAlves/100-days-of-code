class Livro:
    def __init__(self, titulo, num_paginas):
        self._titulo = titulo
        self._num_paginas = num_paginas
        self._titulo_anterior = None

    def __repr__(self):
        return '%s, %s ->  %s' % (self._titulo, self._num_paginas, self._titulo_anterior)
