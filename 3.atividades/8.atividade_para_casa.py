import os
os.system ("clear")

#ATIVIDADE PARA CASA
#ELABORE UM ALGORITMO USANDO OPERAÇÕES PARA INFORMAR SE UMA PESSOA É OBRIGADA A VOTAR.
#CONSIDERE QUE A REGRA É QUE MENORES DE 18 E MAIORES QUE 65 NÃO SÃO OBRIGADOS A VOTAR.

# ENTRADA
idade = int(input("Digite sua idade: "))

if idade > 65:
    print("Não são obrigados a votar!")
if idade < 18:
    print("Não são obrigados a votar!")
else:
    print("São obrigados a votar!")