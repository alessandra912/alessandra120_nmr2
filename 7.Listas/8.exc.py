import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

print(f"\n==Solicitando Números==")
for i in range(QUANTIDADE_NUMEROS):
    numeros = float(input(f"Digite um {i+1}º número: "))
    lista_numeros.append(numeros)

#Verificando meior e menor número em uma lista.
#As funções max() e min() percorrem o vetor e mostram o maior e 
#O menor número respectivamente.
menor = min(lista_numeros)
maior = max(lista_numeros)

print(f"\n==Mostrando números==")
#Usando ForEach numerando os elementos da lista.
#Iniciando contagem com a variável i, começando com o número 1.
for i, numeros in enumerate(lista_numeros, start=1): 
    print(f"{i}º Número:", numeros)

print(f"\nNúmero maior:", maior)
print("Número menor:", menor)