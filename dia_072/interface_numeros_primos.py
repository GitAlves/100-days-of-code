import tkinter as tk

root = tk.Tk()
root.title('Verificador de números primos')

label = tk.Label(root, text='Digite um número:')
label.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()
