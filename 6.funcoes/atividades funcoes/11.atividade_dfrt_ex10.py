import os
os.system("cls || clear")

soma = 0

def calcular(soma):
    return soma / 3

for i in range(3):
    notas = int(input(f"Digite uma nota: "))
    soma += notas

media = calcular(soma) 

print(f"Média: {media}")