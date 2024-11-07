from tkinter import *
from tkinter import ttk

# Criando janela
root = Tk()

# Título da janela do app
root.title("Jogo de Perguntas e Respostas")

# Lista de perguntas e respostas
perguntas = [
    {"pergunta": "Qual é a capital da França?", "respostas": ["Paris", "Londres", "Berlim", "Roma"], "correta": "Paris"},
    {"pergunta": "Qual o maior planeta do sistema solar?", "respostas": ["Terra", "Marte", "Júpiter", "Saturno"], "correta": "Júpiter"},
    {"pergunta": "Quem escreveu 'Dom Quixote'?", "respostas": ["William Shakespeare", "Miguel de Cervantes", "Dante Alighieri", "Jorge Luis Borges"], "correta": "Miguel de Cervantes"},
    {"pergunta": "Qual é o elemento químico representado pelo símbolo 'O'?", "respostas": ["Ouro", "Oxigênio", "Osmium", "Organium"], "correta": "Oxigênio"}
]

# Variáveis globais
indice_pergunta = 0
pontuacao = 0

# Função para verificar a resposta
def verificar_resposta():
    global indice_pergunta, pontuacao
    resposta_selecionada = opcao_selecionada.get()
    if resposta_selecionada == perguntas[indice_pergunta]["correta"]:
        resultado.set("Correto!")
        pontuacao += 1
    else:
        resultado.set(f"Errado! A resposta correta é {perguntas[indice_pergunta]['correta']}")
    
    indice_pergunta += 1
    if indice_pergunta < len(perguntas):
        mostrar_pergunta()
    else:
        fim_do_jogo()

# Função para exibir a próxima pergunta
def mostrar_pergunta():
    pergunta_atual = perguntas[indice_pergunta]
    pergunta.set(pergunta_atual["pergunta"])
    
    for i, resposta in enumerate(pergunta_atual["respostas"]):
        botoes_resposta[i].config(text=resposta, value=resposta)

    resultado.set("")

# Função para mostrar a pontuação final e encerrar o jogo
def fim_do_jogo():
    pergunta.set(f"Fim de jogo! Sua pontuação final: {pontuacao}/{len(perguntas)}")
    for botao in botoes_resposta:
        botao.pack_forget()
    botao_verificar.pack_forget()

# Criando as divisões do App
mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

# Variáveis
pergunta = StringVar()
resultado = StringVar()
opcao_selecionada = StringVar()

# Labels
ttk.Label(mainframe, textvariable=pergunta, wraplength=400).grid(column=0, row=0, columnspan=4, sticky=(W, E))

# Botões de resposta
botoes_resposta = []
for i in range(4):
    botao = ttk.Radiobutton(mainframe, text="", variable=opcao_selecionada, value="")
    botao.grid(column=0, row=i + 1, sticky=(W, E))
    botoes_resposta.append(botao)

# Botão para verificar a resposta
botao_verificar = ttk.Button(mainframe, text="Verificar Resposta", command=verificar_resposta)
botao_verificar.grid(column=0, row=5, sticky=W)

# Label de resultado
ttk.Label(mainframe, textvariable=resultado).grid(column=0, row=6, sticky=(W, E))

# Ajuste de espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

# Iniciar com a primeira pergunta
mostrar_pergunta()

# Gerando loop de render
root.mainloop()


