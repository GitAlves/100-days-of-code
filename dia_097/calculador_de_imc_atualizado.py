import tkinter as tk
from tkinter.ttk import Label, Entry, Button


def calcula_imc(peso, altura):
    imc = round(peso / (altura ** 2), 1)

    if imc < 18.59:
        return [imc, 'abaixo do peso.']
    elif 18.6 < imc < 24.99:
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
        caixa_altura.delete(0, 'end')
        caixa_peso.delete(0, 'end')

        resultado = calcula_imc(peso, altura)

        resultado_imc.config(
            text=f'O resultado do seu imc deu {resultado[0]}.'
        )
        significado_imc.config(
            text=f'Você está {resultado[1]}'
        )


def apenas_numeros(caracter):
    return caracter.isdigit() or caracter == ''


interface = tk.Tk()
interface.title('Calculador de IMC')
interface.geometry('400x300')

texto_peso = Label(
    text='Insira o seu peso (Kg):',
    font=('Arial', 12, 'bold')
)
texto_peso.grid(
    column=0,
    row=0,
    padx=(10, 1.5),
    pady=(40, 10)
)

validacao = (interface.register(apenas_numeros), '%P')

caixa_peso = Entry(
    font=('Arial', 12),
    justify='center',
    validate='key',
    validatecommand=validacao,
)
caixa_peso.grid(
    column=1,
    row=0,
    padx=(1.5, 10),
    pady=(40, 5)
)

texto_altura = Label(
    text='Insira a sua altura (cm):',
    font=('Arial', 12, 'bold')
)
texto_altura.grid(
    column=0,
    row=1,
    padx=(10, 1.5),
    pady=10
)

caixa_altura = Entry(
    font=('Arial', 12),
    justify='center',
    validate='key',
    validatecommand=validacao,
)
caixa_altura.grid(
    column=1,
    row=1,
    padx=(1.5, 10),
    pady=10
)

botao_verificar = Button(
    text='Verificar',
    command=verificar_valores,
    width=20
)
botao_verificar.grid(
    column=0,
    row=2,
    padx=5,
    pady=10,
    columnspan=2
)

resultado_imc = Label(
    text='',
    font=('Times', 14)
)
resultado_imc.grid(
    column=0,
    row=3,
    padx=5,
    pady=(20, 0),
    columnspan=2
)

significado_imc = Label(
    text='',
    font=('Times', 14)
)
significado_imc.grid(
    column=0,
    row=4,
    padx=5,
    pady=(0, 10),
    columnspan=2
)

botao_sair = Button(
    text='Sair',
    command=quit
)
botao_sair.grid(
    column=0,
    row=5,
    padx=150,
    pady=(10, 20),
    columnspan=2
)

interface.mainloop()
