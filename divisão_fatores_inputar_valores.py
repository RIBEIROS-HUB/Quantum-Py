def dividir(numero,divisor):
    if divisor == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return numero / divisor

sobra_divisão = dividir(int(input("Digite o Número a ser  divido:")), int(input("Digite o Número divisor:")))
print(sobra_divisão)