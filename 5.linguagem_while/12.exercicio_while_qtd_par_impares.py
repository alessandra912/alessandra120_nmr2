#Faça um algoritmo que leia uma quantidade não
#determinada de números inteiros positivos. Calcule: 
#a) quantidade de números pares e ímpares; 
#b) média de valores pares 
#c) média geral dos números lidos. 
#O número que encerrará a leitura será o número zero.

import os
os.system("cls | clear")

contador = 0
soma_pares = 0
quantidades_pares = 0
quantidade_impares = 0
soma_geral = 0


while True:
        numero = int(input(f"Digite {contador + 1}º um número: "))

        if numero == 0:
            break
        if numero % 2 == 0:
            quantidades_pares += 1
            soma_pares += numero
        else:
            quantidade_impares += 1

        contador += 1
        soma_geral += numero
            
media_pares = soma_pares / quantidades_pares
media_geral = soma_geral / contador

print(f"\nNumeros pares: {quantidade_impares}")
print(f"Números impares: {quantidade_impares}")
print(f"\nMédia pares: {media_pares}")
print(f"Média: {media_geral}")