import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numeros = float(input("Digite um número: "))
    lista_numeros.append(numeros)

menor = min(lista_numeros)
maior = max(lista_numeros)

print()
for numeros in lista_numeros: 
    print("Número:", numeros)

print("Número maior:", maior)
print("Número menor:", menor)