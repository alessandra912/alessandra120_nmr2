import os
os.system("cls || clear")

soma = 0

def calcular(soma):
    if soma <= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")
    resultado = soma / 2
    return resultado

for i in range(2):
    notas = int(input(f"Digite uma nota: "))
    soma += notas

media = calcular(soma) 

print(f"Média: {media}")