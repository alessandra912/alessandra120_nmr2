import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 6
contador = 0
quantidades_pares = 0
quantidade_impares = 0


print(f"\n==Solicitando Números==")
for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input(f"Digite um {i + 1}º número: "))
    lista_numeros.append(numeros)

    if numeros == 0:
            break
    if numeros % 2 == 0:
        quantidades_pares += 1
    else:
        quantidade_impares += 1

        contador += 1

print(f"\n==Mostrando números==")
for i, numeros in enumerate (lista_numeros, start = 1): 
    print(f"{i}º Número:", numeros)

print(f"\nNúmeros Pares:", quantidades_pares)
print("Números impares:", quantidade_impares)