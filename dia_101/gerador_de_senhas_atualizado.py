from random import choice as ch
import string


def caractere_aleatorio():
    lista_caracteres = str(
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    categoria_escolhida = ch(lista_caracteres)

    return ch(categoria_escolhida)


quantidade_caracteres = int(
    input(
        'Insira qual a quantidade de caracteres que a senha deverá ter: '
    )
)

senha = ''
for i in range(quantidade_caracteres):
    senha += caractere_aleatorio()

print(f'\nA senha sugerida foi: {senha}')
