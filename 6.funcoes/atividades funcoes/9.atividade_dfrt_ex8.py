import os
from datetime import date
os.system("cls || clear")

def calcular(ano_de_nascimeto):
    resultado = date.today().year - ano_de_nascimeto
    return resultado

ano_de_nascimento = int(input("Digite seu ano de nascimeto: "))

idade = calcular(ano_de_nascimento)

print(f"Idade: {idade}")