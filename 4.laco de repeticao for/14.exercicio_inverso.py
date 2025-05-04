# Escrever um programa de computador que do usuário de 3 notas e, ao final, apresente
# a media e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado.
# Considere que para a aprovação, deve-se obter média maior ou igual a 7, para ser reprovado,
# a média deve ser menor que 4

import os

os.system ("cls || clear")

print("MEDIA DAS NOTAS")

soma = 0

for i in range(3):
    notas = float(input(f"Digite uma nota: "))
    soma += notas

media = soma / 3

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado!")
elif media >= 4:
    print("Recuperação!")
else:
    print("Reprovado!")