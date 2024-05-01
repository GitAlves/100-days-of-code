class Jogo:
    def __init__(self):
        self._jogadores = dict()

    def __repr__(self):
        return str(self._jogadores)

    def apresentar_dados_jogador(self, jogador):
        return self._jogadores[jogador]

    def adicionar_novo_jogador(self, nome, pontos):
        if len(self._jogadores) == 0:
            self._jogadores["jogador1"] = {'nome': nome, 'pontos': pontos}
        else:
            self._jogadores[
                "jogador" + str(len(self._jogadores) + 1)
                ] = {'nome': nome, 'pontos': pontos}

    def atualizar_pontuacao(self, nome_jogador, nova_pontuacao):
        if nome_jogador in str(self._jogadores):
            for jogador in self._jogadores.values():
                if jogador['nome'] == nome_jogador:
                    jogador['pontos'] = nova_pontuacao
        elif self._jogadores is None:
            print('Não há jogadores cadastrados no sistema!')
        else:
            print(f'"{nome_jogador}" ainda não foi cadastrado! no sistema')

    def remover_jogador(self, nome):
        if nome in str(self._jogadores):
            for jogador in self._jogadores:
                if self._jogadores[jogador]['nome'] == nome:
                    del self._jogadores[jogador]
                    break
        elif self._jogadores is None:
            print('Não há jogadores cadastrados no sistema!')
        else:
            print(f'"{nome}" ainda não foi cadastrado no sistema!')

    def apresentar_jogadores(self):
        if self._jogadores is not None:
            for jogador in self._jogadores:
                print(f'\n\n-------- {jogador} ------------\n')
                print(f"Nome: {self._jogadores[jogador]['nome']}\n")
                print(f"Pontuação: {self._jogadores[jogador]['pontos']}\n\n")
        else:
            print('Não há jogadores para serem mostrados!')
