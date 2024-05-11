def chamar_fibonacci(vezes):
    anterior = 0
    atual = 1
    auxiliar = 0

    while vezes:
        print(atual, end=' ')

        auxiliar = anterior + atual
        anterior = atual
        atual = auxiliar

        vezes -= 1
