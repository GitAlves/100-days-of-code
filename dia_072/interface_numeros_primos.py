import tkinter as tk
from tkinter import messagebox, ttk
from numeros_primos_versao_atualizada import numero_primo


def verificar_numero():
    numero = int(entry.get())
    numero_verificado = numero_primo(numero)

    if numero_verificado is True:
        botao_primo.config(style='Certo.TButton')
        botao_nao_primo.config(style='TButton')
        messagebox.showinfo('Resultado', f'{numero} é um número primo!')
    else:
        botao_nao_primo.config(style='Errado.TButton')
        botao_primo.config(style='TButton')
        messagebox.showinfo('Resultado', f'{numero} não é um número primo.')


def limpar():
    botao_primo.config(style='TButton')
    botao_nao_primo.config(style='TButton')
    entry.delete(0, tk.END)


root = tk.Tk()
root.title('Verificador de números primos')
root.geometry('400x300')
root.config(bg='yellow')

style = ttk.Style()
style.configure('Certo.TButton', background='green')
style.configure('Errado.TButton', background='red')

label = ttk.Label(root, text='Digite um número:', font='arial 12', background='yellow')  # noqa: E501;
label.grid(column=0, row=0, padx=5, pady=30)

entry = ttk.Entry(root, justify='center')
entry.grid(column=1, row=0, padx=5, pady=30)

botao_verificar = ttk.Button(root, text='Verificar', command=verificar_numero)
botao_verificar.grid(column=2, row=0, padx=5, pady=30)

pergunta_numero_primo = ttk.Label(root, text='Este número é primo?', font='arial 12', background='yellow')  # noqa: E501;
pergunta_numero_primo.grid(column=1, row=1, padx=5, pady=15)

botao_primo = ttk.Button(root, text='✓', style='TButton', state=tk.DISABLED)
botao_primo.grid(column=0, row=2, padx=0, pady=0)

botao_nao_primo = ttk.Button(root, text='✗', style='TButton', state=tk.DISABLED)  # noqa: E501;
botao_nao_primo.grid(column=2, row=2, padx=0, pady=0)

novo_numero = ttk.Button(root, text='Testar outro número', command=limpar)
novo_numero.grid(column=1, row=3, padx=5, pady=80)

root.mainloop()
