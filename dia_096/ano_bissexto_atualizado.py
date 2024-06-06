def validador(ano: int):
    if ano % 4 == 0:
        return f'{ano} é um ano bissexto!'
    else:
        return f'{ano} não é um ano bissexto!'


ano_escolhido = int(input('Insira um ano qualquer: '))
print(validador(ano_escolhido))
