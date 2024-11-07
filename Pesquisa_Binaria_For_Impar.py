def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    tamanho_inicial = len(lista)  # Armazena o tamanho inicial da lista

    for _ in range(len(lista)):
        meio = (baixo + alto) // 2
        chute = lista[meio]

        # Calcula quantos elementos foram descartados
        elementos_restantes = alto - baixo + 1
        descartados = tamanho_inicial - elementos_restantes
        print(f"Elementos descartados até agora: {descartados}")

        if chute == item:
            return meio  # Retorna o índice se o item for encontrado
        elif chute > item:
            alto = meio - 1  # Reduz o intervalo superior
        else:
            baixo = meio + 1  # Aumenta o intervalo inferior

    return -1  # Retorna -1 se o item não for encontrado

# Lista de 200 elementos ordenados
listaComDuzentos = list(range(1, 401, 2))  # Gera uma lista de 200 números ímpares (1, 3, 5, ..., 399)

# Executa a busca e imprime o resultado
indice = pesquisa_binaria(listaComDuzentos,251 )
print(f"O índice do número buscado é: {indice}")