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


quantidade_caracteres = 0
resp = 'N'
while resp != 'S':
    try:
        quantidade_caracteres = int(
            input(
                '\n\nInsira qual a quantidade de caracteres que a senha deverá ter: '  # noqa: E501;
            )
        )
    except ValueError:
        print('\n\nInsira um número inteiro para definir o tamanho da senha!')
    else:
        senha = gerar_senha(quantidade_caracteres)

        print(f'\n\nA senha sugerida foi: {senha}')

        while True:
            resp = input('\n\nGostaria de sair [S/N]: ')

            match resp:
                case 'S':
                    break
                case 'N':
                    break
                case _:
                    print('\n\nDigite [S] para sair ou [N] para pedir mais uma senha!')  # noqa: E501;


print('\n\nFoi um prazer!\n\n')
