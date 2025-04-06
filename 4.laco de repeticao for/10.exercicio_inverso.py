# Escreva um algoritmo que solicite ao usuário 5 valores inteiros e ao final mostre:
# a. quantos números são pares;
# b. quantos números são impares;

import os

os.system ("cls || clear")


pares = 0
impares = 0

print("IMPARES E PARES")

for i in range(5):
    numero = int(input(f"Digite um número: "))
    if numero % 2 == 0:
        pares += 1
        # Or
        # pares + pares = 1
    else:
        impares += 1
        # Or
        # impares + impares = 1

print()
print(f"Pares: {pares}")
print(f"Impares: {impares}")

print(f"\nFIM DO PROGRAMA")
