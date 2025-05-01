import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numeros)

menor = min(lista_numeros)
maior = max(lista_numeros)

print("\nNúmero maior:", maior)
print("Número menor:", menor)