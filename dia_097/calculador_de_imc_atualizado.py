import tkinter as tk


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
    

def verificar_valores(peso, altura):
    ...


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

caixa_peso = tk.Entry()
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

caixa_altura = tk.Entry()
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
    text='O resultado IMC virá aqui!'
)
resultado_imc.grid(
    column=0,
    row=3,
    padx=5,
    pady=10,
    columnspan=2
)

interface.mainloop()
