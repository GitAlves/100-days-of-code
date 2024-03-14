from random import choice as ch
from palavras import lista_frutas

palavra = ch(lista_frutas)
palavra_escondida = '_' * len(palavra)

print(palavra_escondida)

tentativas = 10

while tentativas:
    chute = input('Chute uma letra: ')

    if chute in palavra:
        posicao = palavra.index(chute)

        palavra_atualizada = ''
        contador = 0

        for letra in palavra_escondida:
            if contador == posicao:
                palavra_atualizada = palavra_atualizada + chute
            else:
                palavra_atualizada = palavra_atualizada + letra
            contador += 1

        palavra_escondida = palavra_atualizada
        print(palavra_escondida)

    if palavra == palavra_escondida:
        print('Meus parabéns! Você ganhou.')
        break
