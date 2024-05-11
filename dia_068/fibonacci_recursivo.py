anterior = 0
atual = 1
auxiliar = 0
vezes = 5  # Os 5 primeiros números da sequência de Fibonacci serão mostrados

while vezes:
    print(atual, end=' ')

    auxiliar = anterior + atual
    anterior = atual
    atual = auxiliar

    vezes -= 1

print('\nIsso é tudo por hoje pessoal!')
