# Escrever um programa de computador que solicite do usuário cinco números inteiros e,
# ao final, apresente a soma de todos os números lidos.

import os
os.system ("cls || clear")

print("SOMANDO NÚMEROS:")

soma = 0
for i in range(5):
    nota = int(float(input(f"Digite um número inteiro: ")))
    soma = soma + nota
    # or
    # soma += nota

print()
print(f"Soma: {soma}")


print(f"\nFIM DO PROGRAMA")