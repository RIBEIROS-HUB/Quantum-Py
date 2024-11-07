def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é calculável.")
    return a / b

def calculadora():
    print("Calculadora Simples")
    print("Selecione a operação:")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")

    while True:
        try:
            operacao = input("Escolha uma operação (1/2/3/4): ")

            if operacao not in ['1', '2', '3', '4']:
                raise ValueError("Operação inválida. Por favor, escolha 1, 2, 3 ou 4.")

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '1':
                resultado = soma(num1, num2)
                print(f"O resultado da sua adição é: {num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = subtracao(num1, num2)
                print(f"O resultado da sua subtração é: {num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = multiplicacao(num1, num2)
                print(f"O resultado da sua multiplição é: {num1} * {num2} = {resultado}")
            elif operacao == '4':
                resultado = divisao(num1, num2)
                print(f"O resultado da sua divisão é: {num1} / {num2} = {resultado}")

            break  # Encerrar o loop após uma operação bem-sucedida
        except ValueError as e:
            print(e)
            print("Tente novamente")

if __name__ == "__main__":
    calculadora()
    print("Obrigado por utilizar a nossa calculadora! 😉")