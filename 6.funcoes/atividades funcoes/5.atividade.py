import os
os.system("cls || clear")

def somar(numero_1, numero_2):
    return numero_1 + numero_2

def subtrair(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2

def dividir(numero_1, numero_2):
    return numero_1 / numero_2

numero_1 = int(input("Digite o primeiro número: "))

numero_2 = int(input("Digite o segundo número: "))

soma = somar(numero_1, numero_2)
subtracao = subtrair(numero_1, numero_2)
multiplicacao = multiplicar(numero_1, numero_2)
divisao = dividir(numero_1, numero_2)


print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.2f}")