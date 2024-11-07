from tkinter import *
from tkinter import ttk

# Criando janela
root = Tk()

# Título da janela do app
root.title("Calculadora de IMC")

# Função de cálculo do IMC
def calculate_imc(*args):
    try:
        altura = float(height.get())
        peso = float(weight.get())
        imc_result = peso / (altura ** 2)
        imc.set(f"{imc_result:.2f}")  # Limita o IMC a duas casas decimais
    except ValueError:
        imc.set("Erro")

# Criando as divisões do App
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variáveis
height = StringVar()
weight = StringVar()
imc = StringVar()

# Campo de entrada (altura)
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=2, row=1, sticky=(W, E))

# Campo de entrada (peso)
weight_entry = ttk.Entry(mainframe, width=7, textvariable=weight)
weight_entry.grid(column=2, row=2, sticky=(W, E))

# Labels
ttk.Label(mainframe, text="Altura (m)").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Peso (kg)").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Seu IMC é").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, textvariable=imc).grid(column=2, row=3, sticky=(W, E))

# Botão de cálculo
ttk.Button(mainframe, text="Calcular", command=calculate_imc).grid(column=2, row=4, sticky=W)

# Ajuste de espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Foco no campo de entrada
height_entry.focus()

# Vinculando a tecla Enter à função de cálculo
root.bind("<Return>", calculate_imc)

# Gerando loop de render
root.mainloop()
