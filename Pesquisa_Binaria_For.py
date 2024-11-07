def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    # Usando um 'for' para limitar o número de tentativas de busca
    for _ in range(len(lista)):
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio  # Retorna o índice se o item for encontrado
        elif chute > item:
            alto = meio - 1  # Reduz o intervalo superior
        else:
            baixo = meio + 1  # Aumenta o intervalo inferior

    return -1  # Retorna -1 se o item não for encontrado

# Lista de 100 elementos ordenados
listaComCem = [
    6, 8, 15, 16, 27, 36, 44, 44, 50, 51, 68, 82, 89, 99, 105, 108, 111, 128, 129, 141, 150,
    151, 153, 162, 180, 197, 213, 239, 252, 264, 273, 275, 293, 322, 340, 343, 348, 351, 353,
    356, 357, 368, 370, 381, 387, 387, 410, 428, 432, 437, 474, 500, 535, 544, 551, 568, 569,
    580, 584, 594, 605, 625, 650, 653, 659, 667, 673, 685, 691, 698, 720, 744, 745, 749, 782,
    791, 797, 806, 817, 819, 821, 822, 850, 850, 870, 870, 885, 908, 912, 913, 917, 917, 926,
    931, 944, 966, 972, 991, 998
]

# Executa a busca e imprime o resultado
indice = pesquisa_binaria(listaComCem, 998)
print(f"O índice do número buscado é: {indice}")