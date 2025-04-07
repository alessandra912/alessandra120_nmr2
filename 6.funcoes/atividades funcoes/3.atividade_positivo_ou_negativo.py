#Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo.
import os
os.system("cls || clear")

def positivo_ou_negativo(valor):
    if valor >= 1:
        print("Valor positivo")
    elif valor == 0:
        print("Número neutro")
    else:
        print("Valor negativo")

print("= Positivos ou negativos =")
valor = int(input("Digite um número: "))
positivo_ou_negativo(valor)
