def idade_voto_eleição_presidencial(idade):
    if idade >= 16:
        return "Você pode votar."
    else:
        return "Você não pode votar."

idade_eleitor = int(input("Digite a sua idade: "))
apto_para_votar = idade_voto_eleição_presidencial(idade_eleitor)
print(apto_para_votar)