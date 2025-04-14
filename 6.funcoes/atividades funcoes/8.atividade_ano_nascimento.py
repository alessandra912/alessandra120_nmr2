import os
os.system("cls || clear")

def calcular(ano_de_nascimeto):
    resultado = 2025 - ano_de_nascimeto
    return resultado

idade = int(input("Digite seu ano de nascimeto: "))

idade = calcular(idade)

print(f"Idade: {idade}")
