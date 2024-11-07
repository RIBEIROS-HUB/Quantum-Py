
from tkinter import *
from tkinter import ttk

# Criando janela
root = Tk()

# Título da janela do app
root.title("Conversor de Pés para Metros")

# Função de conversão de pés para metros
def calculate(*args):
    try:
        value = float(feet.get())
        result =  int (0.3048 * value * 10000.0 + 0.5)/10000.0  
    except ValueError:
        result("Erro")

# Criando as divisões do App
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variáveis
feet = StringVar()
meters = StringVar()

# Campo de entrada (pés)
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Labels

ttk.Label(mainframe, text="pés").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é igual a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)

# Botão de conversão
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=2, row=3, sticky=W)

# Ajuste de espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Foco no campo de entrada
feet_entry.focus()

# Vinculando a tecla Enter à função de cálculo
root.bind("<Return>", calculate)

# Gerando loop de render
root.mainloop()
