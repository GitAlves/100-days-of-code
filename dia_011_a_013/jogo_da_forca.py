from random import choice as ch
from palavras import lista_frutas


def lembrete_tentativas(numero):
    return f'\n--------- TENTATIVAS: {numero} -------------\n'


palavra = ch(lista_frutas)
palavra_escondida = '_' * len(palavra)

tentativas = 10
print(lembrete_tentativas(tentativas))

while tentativas:
    print(palavra_escondida)

    chute = input('\nChute uma letra: ')

    if chute in palavra:
        print('\nLETRA ENCONTRADA!!!\n')

        rascunho = list(palavra_escondida)

        for posicao, letra in enumerate(palavra):
            if letra == chute:
                rascunho[posicao] = letra

        palavra_escondida = ''.join(rascunho)
    else:
        tentativas -= 1
<<<<<<< HEAD
        print('Errou!')
=======
        print('\nErrou!')
>>>>>>> 7a096fd4722732d439d660a7fc8bd46896a17361
        print(lembrete_tentativas(tentativas))

    if palavra == palavra_escondida:
        print('Meus parabéns! Você ganhou.')
        break

if tentativas == 0:
    print(f'Game over!\nA palavra era "{palavra}".')
