import os
os.system("cls || clear")

lista_numeros = []
NUMEROS = 5

for i in range (NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < 0:
       numero = 0
    lista_numeros.append(numero)

for numero in lista_numeros:
    print(f"\nNúmero: {numero}")