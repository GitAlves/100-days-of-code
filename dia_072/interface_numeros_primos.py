import tkinter as tk
from tkinter import ttk
from numeros_primos_versao_atualizada import numero_primo


def verificar_numero():
    numero = int(entry.get())
    numero_verificado = numero_primo(numero)
    entry.config(state=tk.DISABLED)
    botao_verificar.config(state=tk.DISABLED)

    if numero_verificado is True:
        botao_primo.config(style='Certo.TButton')
        botao_nao_primo.config(style='TButton')
    else:
        botao_nao_primo.config(style='Errado.TButton')
        botao_primo.config(style='TButton')


def limpar():
    botao_primo.config(style='TButton')
    botao_nao_primo.config(style='TButton')
    entry.config(state=tk.ACTIVE)
    botao_verificar.config(state=tk.ACTIVE)
    entry.delete(0, tk.END)


def apenas_numeros(caracter):
    return caracter.isdigit() or caracter == ''


root = tk.Tk()
root.title('Verificador de números primos')
root.geometry('400x300')
root.config(bg='yellow')

style = ttk.Style()
style.configure('Certo.TButton', background='green')
style.configure('Errado.TButton', background='red')

label = ttk.Label(root, text='Digite um número:', font='arial 12', background='yellow')  # noqa: E501;
label.grid(column=0, row=0, padx=5, pady=30)

validacao = (root.register(apenas_numeros), '%P')

entry = ttk.Entry(root, justify='center', validate='key', validatecommand=validacao)  # noqa: E501;
entry.grid(column=1, row=0, padx=5, pady=30)

botao_verificar = ttk.Button(root, text='Verificar', command=verificar_numero)
botao_verificar.grid(column=2, row=0, padx=5, pady=30)

pergunta_numero_primo = ttk.Label(root, text='Este número é primo?', font='arial 12', background='yellow')  # noqa: E501;
pergunta_numero_primo.grid(column=0, row=1, padx=5, pady=15, columnspan=3, sticky='NS')  # noqa: E501;

botao_primo = ttk.Button(root, text='✓', style='TButton', state=tk.DISABLED)
botao_primo.grid(column=0, row=2, padx=0, pady=0)

botao_nao_primo = ttk.Button(root, text='✗', style='TButton', state=tk.DISABLED)  # noqa: E501;
botao_nao_primo.grid(column=2, row=2, padx=0, pady=0)

novo_numero = ttk.Button(root, text='Testar outro número', command=limpar)
novo_numero.grid(column=0, row=3, padx=5, pady=80, columnspan=3, sticky='NS')

root.mainloop()
