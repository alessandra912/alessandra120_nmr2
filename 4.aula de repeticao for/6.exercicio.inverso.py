# Escrever um algoritmo que solicite ao usuário um número e faça a contagem
# regressiva a partir do número informado até o número 1, 
# aguardando um segundo para mostrar cada número.

import os
import time

os.system ("cls || clear")

print("CONTAGEM REGRESSIVA")
numero = int(input("Digite um número para contagem regressiva: "))

for i in range (numero, 0, -1):
    print(i)
    time.sleep(1)

print("FIM DO PROGRAMA") 