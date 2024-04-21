class Pedido:
    def __init__(self, numero_pedido, cliente, itens_pedido, valor):
        self.numero_pedido = numero_pedido
        self.nome_cliente = cliente
        self.itens_pedido = itens_pedido
        self.valor = valor
        self.proximo_pedido = None

    def __repr__(self):
        return '%s, %s, %s, %s -> %s' % (
            self.numero_pedido,
            self.nome_cliente,
            self.itens_pedido,
            self.valor,
            self.proximo_pedido
        )


class FilaDePedidos:
    def __init__(self):
        self.pedido = None

    def adicionar_pedido(self, numero, cliente, itens, valor):
        novo_pedido = Pedido(numero, cliente, itens, valor)
        if self.pedido is None:
            self.pedido = novo_pedido
        else:
            fila = self.pedido

            while fila:
                if fila.proximo_pedido is None:
                    fila.proximo_pedido = novo_pedido
                    break
                fila = fila.proximo_pedido

    def remover_primeiro_pedido(self):
        if self.pedido is None:
            print('Sem pedidos na fila. Bora descansar ;)')
        else:
            fila = self.pedido
            self.pedido = fila.proximo_pedido
