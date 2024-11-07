def mediana_idades(idade1, idade2, idade3):
    idades = [idade1, idade2, idade3]
    idades.sort()
    return idades[1]
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))
mediana = mediana_idades(idade1, idade2, idade3)
print(f"A idade de Camila é: {mediana}")


