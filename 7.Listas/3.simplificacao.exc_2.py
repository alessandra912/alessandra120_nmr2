#Crie um programa  que leia 3 notas, armazenando em um vetor e calcule a média aritmética.
#Mostre as 3 notas informadas pelo usuário e informe a média.
import os
os.system("cls || clear")
QUANTIDADE_NOTAS = 3

lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADE_NOTAS 

print()
for nota in lista_notas: 
    print("Nota:", nota)

print("Média:", media)