# Escreva um algoritmo que solicite do usuário um número e mostre a tabuada
# de multiplicação do número informado.
# Exemplo:
# 5x1=5
# 5x2=10
# 5x3=15
#
# 5x10=50

import os

os.system ("cls || clear")

numero = int(input("Digite um número para a tabuada: "))

for i in range (1, 11):
    print(f"{numero} x {i} - {numero * i}")

print("FIM DO PROGRAMA")    