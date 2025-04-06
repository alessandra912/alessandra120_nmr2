# Escrever um programa de computador que solicite do 
# usuário 4 notas e, ao final apresente a média.

import os

os.system ("cls || clear")

print("MEDIA DAS NOTAS")

soma = 0

for i in range(4):
    notas = float(input(f"Digite uma nota: "))
    soma += notas

media = soma / 4


print()
print(f"Média: {media}")

print(f"\nFIM DO PROGRAMA")