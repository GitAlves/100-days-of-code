import tkinter as tk
from tkinter import messagebox
from numeros_primos_versao_atualizada import numero_primo


def verificar_numero():
    numero = int(entry.get())
    numero_verificado = numero_primo(numero)

    if numero_verificado is True:
        botao_primo.config(bg='green')
        botao_nao_primo.config(bg='grey')
        messagebox.showinfo('Resultado', f'{numero} é um número primo!')
    else:
        botao_nao_primo.config(bg='red')
        botao_primo.config(bg='grey')
        messagebox.showinfo('Resultado', f'{numero} não é um número primo.')


root = tk.Tk()
root.title('Verificador de números primos')

label = tk.Label(root, text='Digite um número:')
label.pack()

entry = tk.Entry(root)
entry.pack()

botao_verificar = tk.Button(root, text='Verificar', command=verificar_numero)
botao_verificar.pack()

botao_primo = tk.Button(root, text='✓', bg='grey', state=tk.DISABLED)
botao_primo.pack()

botao_nao_primo = tk.Button(root, text='✗', bg='grey', state=tk.DISABLED)
botao_nao_primo.pack()

novo_numero = tk.Button(root, text='Testar outro número', command=limpar)
novo_numero.pack()

root.mainloop()
