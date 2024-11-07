def dividir(numero,divisor):
    if divisor == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return numero / divisor

sobra_divisão = dividir(10, 6)
print(sobra_divisão)