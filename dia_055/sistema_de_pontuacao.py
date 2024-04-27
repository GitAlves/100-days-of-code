class Jogo:
    def __init__(self):
        self._jogadores = dict()

    def __repr__(self):
        return str(self._jogadores)

    def adicionar_novo_jogador(self, nome, pontos):
        if len(self._jogadores) == 0:
            self._jogadores["jogador1"] = {'nome': nome, 'pontos': pontos}
        else:
            self._jogadores[
                "jogador" + str(len(self._jogadores) + 1)
                ] = {'nome': nome, 'pontos': pontos}
