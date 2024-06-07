import tkinter as tk


def calcula_imc(peso, altura):
    imc = round(peso / (altura ** 2), 1)

    if imc < 18.5:
        return [imc, 'abaixo do peso.']
    elif 18.6 < imc < 24.9:
        return [imc, 'no peso ideal. Meus parabéns!']
    elif 25 < imc < 29.99:
        return [imc, 'com um leve sobrepeso.']
    else:
        return [imc, 'em um grau de obesidade.']


def verificar_valores():
    try:
        peso = int(caixa_peso.get())
        altura = (int(caixa_altura.get())) / 100
    except ValueError:
        pass
    else:
        resultado = calcula_imc(peso, altura)

        resultado_imc.config(
            text=f'O resultado do seu imc deu {resultado[0]}.\nVocê está {resultado[1]}'  # noqa: E501;
        )


def apenas_numeros(caracter):
    return caracter.isdigit() or caracter == ''


interface = tk.Tk()
interface.title('Calculador de IMC')
interface.geometry('400x300')

texto_peso = tk.Label(
    text='Insira o seu peso'
)
texto_peso.grid(
    column=0,
    row=0,
    padx=5,
    pady=10
)

validacao = (interface.register(apenas_numeros), '%P')

caixa_peso = tk.Entry(
    validate='key',
    validatecommand=validacao
)
caixa_peso.grid(
    column=1,
    row=0,
    padx=5,
    pady=10
)

texto_altura = tk.Label(
    text='Insira a sua altura'
)
texto_altura.grid(
    column=0,
    row=1,
    padx=5,
    pady=10
)

caixa_altura = tk.Entry(
    validate='key',
    validatecommand=validacao
)
caixa_altura.grid(
    column=1,
    row=1,
    padx=5,
    pady=10
)

botao_verificar = tk.Button(
    text='Verificar',
    command=verificar_valores
)
botao_verificar.grid(
    column=0,
    row=2,
    padx=5,
    pady=10,
    columnspan=2
)

resultado_imc = tk.Label(
    text=''
)
resultado_imc.grid(
    column=0,
    row=3,
    padx=5,
    pady=10,
    columnspan=2
)

interface.mainloop()
