#Construa um algoritmo que calcule a média aritmética de vários valores 
#inteiros positivos, inseridos pelo usuário. 
#O final da leitura acontecerá quando for lido um valor negativo.
#Mostre a média aritmética dos números informados pelo usuário.


import os

os.system("cls | clear")


soma = 0
contador = 0

while True:
    valor = float(input(f"Digite  {contador + 1}º um valor: "))

    if valor < 0:
        break

    else:
        contador += 1
        soma += valor
        
media = soma / contador


print(f"\nMédia: {media}")