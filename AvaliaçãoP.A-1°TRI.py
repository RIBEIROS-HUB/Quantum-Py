tempo = int(input("Digite tempo de viagem: "))
distancia = int(input("Digite distância percorrida: "))
litros = float((tempo * distancia)/12)

i = litros
while i == litros:
  print(f"Quantidade de litros: ", f"{i:.3f}")
  break