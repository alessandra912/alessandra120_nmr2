import os
os.system("cls || clear")

lista_numeros = []

QUANTIDADE_NUMEROS = 6

def pares_impares(lista):
    quantidade_pares = 0
    quantidade_impares = 0
    for numeros in lista:
        if numeros % 2 == 0:
            quantidade_pares += 1
        else:
            quantidade_impares += 1
    return quantidade_pares, quantidade_impares

print(f"\n==Solicitando Números==")
for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input(f"Digite um {i + 1}º número: "))
    lista_numeros.append(numeros)

quantidade_pares, quantidade_impares = pares_impares(lista_numeros)

print(f"\n==Mostrando números==")
for i, numeros in enumerate (lista_numeros, start = 1): 
    print(f"{i}º Número:", numeros)

print(f"\nNúmeros Pares:", quantidade_pares)
print("Números impares:", quantidade_impares)