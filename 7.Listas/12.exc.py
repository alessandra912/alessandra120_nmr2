import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5
soma_positivos = 0
negativos = 0

print(f"\n==Solicitando Números==")
for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input(f"Digite um {i+1}º número: "))
    lista_numeros.append(numeros)

for numeros in lista_numeros:
    if numeros < 0:
        negativos += 1
    else:
        soma_positivos += numeros

print(f"\n==Mostrando números==")
for numeros in lista_numeros: 
    print(f"Números Negativos:", negativos)
    print(f"Números Positivos:", soma_positivos)

print(f"\nNúmeros Negativos:", negativos)
print("Soma de Números positivos:", soma_positivos)