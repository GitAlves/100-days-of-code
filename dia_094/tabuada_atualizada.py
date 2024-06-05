numero_escolhido = int(input('Insira um número para ver a sua tabuada: '))
quantidade = range(
    0, int(
        input(
            'Insira até onde você quer saber da tabuada do número: '
        )
    )
)

lista_numeros = list(map(lambda x: (numero_escolhido, x, x * numero_escolhido), quantidade))  # noqa: E501;

print(lista_numeros)
