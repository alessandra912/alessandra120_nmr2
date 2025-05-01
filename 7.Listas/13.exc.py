import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5

def solicitando_dados():
    lista_numeros = []
    for i in range(QUANTIDADE_NUMEROS):
        numeros = int(input(f"Digite um {i+1}º número: "))
        lista_numeros.append(numeros)
    return lista_numeros

def verificar_positivos_e_negativos(lista):
    soma_positivos = 0
    negativos = 0
    for numeros in lista:
        if numeros < 0:
            negativos += 1
        else:
            soma_positivos += numeros
    return soma_positivos, negativos

lista = solicitando_dados()
soma_positivos, negativos = verificar_positivos_e_negativos(lista)

print(f"\nNúmeros Negativos:", negativos)
print("Soma de Números positivos:", soma_positivos)