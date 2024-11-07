notas = []
for i in range(1, 4):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print("A média das notas é:" , media)
