import os
os.system("cls || clear")

lista_pratos = []
preco_pratos = [] 

while True:

    print("""
========Menu=========
Código\t Prato\t Valor
1   Picanha\t 25,00
2   Lasanha\t 20,00
3   Strognoff\t 18,00
4   Bife acebolado 15,00
5   Pão com ovo\t 5,00""")

    menu = int(input("\nEscolha o código do prato escolhido: "))

    match menu:
        case 1:
            prato = "Picanha"
            preco = 25.00
        case 2:
            prato = "Lasanha"
            preco = 20.00
        case 3:
            prato = "Strogonoff"
            preco = 18.00
        case 4:
            prato = "Bife acebolado"
            preco = 15.00
        case 5:
            prato = "Pão com ovo"
            preco = 5.00
        case _:
            prato = "Opção inválida"
            preco = 0
    
    lista_pratos.append(prato)
    preco_pratos.append(preco)

    continuar = input("""Deseja escolher outro prato?
""").lower()
    if continuar == "Não":
        break
    os.system("cls || clear")

if sum(preco_pratos) == 0:
    print("Nenhum prato foi selecionado")
else:
    print("\n PRATOS ESCOLHIDOS")
    for i, pratos in enumerate(lista_pratos, start=1):
        print(f"{i}º\nPrato:", pratos)

    print(f"\nValor final: R$", preco_pratos)

        