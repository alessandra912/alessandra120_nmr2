#Crie uma função que receba um número e mostre uma mensagem informando se o número é par ou ímpar.
import os
os.system("cls || clear")

def par_ou_impar(numeros):
    if numeros % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")

print("Par ou ímpar")
numero = int(input("Digite um número: "))
par_ou_impar(numero)


