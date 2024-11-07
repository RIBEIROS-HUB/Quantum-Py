# -*- coding: utf-8 -*-
"""def_Phyton.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fFeD66Bdl-TQ60DUY56aIxSoSeRiZmdV
"""

def mediana_idades(idade1, idade2, idade3):
    idades = [idade1, idade2, idade3]
    idades.sort()
    return idades[1]
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))
mediana = mediana_idades(idade1, idade2, idade3)
print(f"A idade de Camila é: {mediana}")

def idade_voto_eleição_presidencial(idade):
    if idade >= 16:
        return "Você pode votar."
    else:
        return "Você não pode votar."

idade_eleitor = int(input("Digite a sua idade: "))
apto_para_votar = idade_voto_eleição_presidencial(idade_eleitor)
print(apto_para_votar)

def dividir(numero,divisor):
    if divisor == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return numero / divisor

sobra_divisão = dividir(10, 6)
print(sobra_divisão)



def dividir(numero,divisor):
    if divisor == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return numero / divisor

sobra_divisão = dividir(int(input("Digite o Número a ser  divido:")), int(input("Digite o Número divisor:")))
print(sobra_divisão)

def dividir(numero, divisor):
    if divisor == 0:
        return "Erro: Por favor, insira valores numéricos válidos."
    return numero / divisor

try:
    numero = float(input("Digite o número a ser dividido: "))
    divisor = float(input("Digite o divisor: "))

    resultado = dividir(numero, divisor)
    print("Resultado da divisão:", resultado)
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")

def dividir(numero, divisor):
    if divisor == 0:
        return "Erro: Divisão por zero não é permitida."
    return numero / divisor

try:
    numero = float(input("Digite o número a ser dividido: "))
    divisor = float(input("Digite o divisor: "))

    resultado = dividir(numero, divisor)
    print("Resultado da divisão:", resultado)
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")

def dividir(numero, divisor):
    try:
        if divisor == 0:
            raise ValueError(" Por favor, insira valores numéricos válidos.")
        return numero / divisor
    except ValueError as sobra_divisão:
        return str(sobra_divisão)

sobra_divisão = dividir(10, 0)
print("A sobra da Divisão dessa é:" , sobra_divisão)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é Calculável.")
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
                print(f"{num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = subtracao(num1, num2)
                print(f"{num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = multiplicacao(num1, num2)
                print(f"{num1} * {num2} = {resultado}")
            elif operacao == '4':
                resultado = divisao(num1, num2)
                print(f"{num1} / {num2} = {resultado}")

            break # Encerrar o loop após uma operação bem-sucedida
        except ValueError as e:
            print(e)
            print("Tente novamente")

if __name__ == "__main__":

  calculadora()
print("Obrigado por utilizar a nossa calculadora! 😉" )