import os
os.system("cls || clear")

def calcular(notas):
    resultado = notas / 3
    return resultado

contador = 0

for i in range(1,4):
    notas = int(input(f"Digite a {i}ª  nota: "))
    contador += notas

media = calcular(contador) 

print(f"Média: {media:.2f}")