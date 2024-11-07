from tkinter import *
from tkinter import ttk

# Criando janela
root = Tk()

# Título da janela do app
root.title("Conversor de Milhas para Quilômetros")

# Função de conversão de milhas para quilômetros
def calculate(*args):
    try:
        value = float(miles.get())
        result = int(1.60934 * value * 10000.0 + 0.5)/10000.0
        kilometers.set(result)
    except ValueError:
        kilometers.set("Erro")

# Criando as divisões do App
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variáveis
miles = StringVar()
kilometers = StringVar()

# Campo de entrada (milhas)
miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)
miles_entry.grid(column=2, row=1, sticky=(W, E))

# Labels
ttk.Label(mainframe, text="milhas").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é igual a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=kilometers).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="quilômetros").grid(column=3, row=2, sticky=W)

# Botão de conversão
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=2, row=3, sticky=W)

# Ajuste de espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Foco no campo de entrada
miles_entry.focus()

# Vinculando a tecla Enter à função de cálculo
root.bind("<Return>", calculate)

# Gerando loop de render
root.mainloop()
