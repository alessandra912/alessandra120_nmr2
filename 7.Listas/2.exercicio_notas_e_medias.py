#Crie um programa  que leia 3 notas, armazenando em um vetor e calcule a média aritmética.
#Mostre as 3 notas informadas pelo usuário e informe a média.
import os
os.system("cls || clear")

lista_notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

soma =sum(lista_notas)
media = soma / 3

print()
for nota in lista_notas: 
    print("Nota:", nota)

print("Média:", media)