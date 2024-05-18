import tkinter as tk

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
