def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return 'abaixo do peso'
    elif 18.6 < imc < 24.9:
        return 'com peso ideal. Meus parabéns!'
    elif 25 < imc < 29.99:
        return 'com um leve sobrepeso'
    else:
        return 'em um grau de obesidade'


peso = float(input('Digite o seu peso [Ex.: 56.7]: '))
altura = float(input('Digite a sua altura em metros [Ex.: 1.54]: '))

print(f'Você está {calcula_imc(peso, altura)}')
