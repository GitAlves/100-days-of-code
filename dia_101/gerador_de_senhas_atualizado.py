from random import choice as ch
import string
from flask import Flask


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


app = Flask('__name__')
