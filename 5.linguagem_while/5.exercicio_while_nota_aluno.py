# Escreva um algoritmo que solicite ao usuário a nota de um aluno. 
# Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
# Mostre a nota informada pelo usuário.

import os

os.system("cls | clear")


QUANTIDADE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_NOTAS):
  while True:
    nota = float(input("Digite sua nota: "))
    
    if nota < 0 or nota > 10:
     print("A nota deve ser entre 0 e 10.\n")
    else:
      soma += nota
      break

media = soma / QUANTIDADE_NOTAS

print(f"Média: {media}")