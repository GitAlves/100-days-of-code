from random import choice as ch
import string


def gerar_senha(quant_caracteres):
    lista_caracteres = str(
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    senha = ''
    while quant_caracteres:
        senha += ch(lista_caracteres)

        quant_caracteres -= 1

    return senha


quantidade_caracteres = int(
    input(
        'Insira qual a quantidade de caracteres que a senha deverá ter: '
    )
)

senha = gerar_senha(quantidade_caracteres)

print(f'\nA senha sugerida foi: {senha}')
