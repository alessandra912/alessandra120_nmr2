#Faça um algoritmo que mostre um menu com
#opções de um cardápio de restaurante para
#uma pessoa. A pessoa vai escolher o prato
#desejado.
#Após escolher o prato, o algoritmo deve
#perguntar ao usuário se ele deseja escolher
#outro prato.
#Calcule quanto deve ser pago pelo cliente.


import os
os.system("cls | clear")


quantidade_de_pratos = 5
soma = 0

while True:
    menu = int(input("""
=========Menu========
codigo  menu \t    valor
1- \t   Picanha \t    25,00
2- \t   Lasanha \t    20,00
3- \t   Strogonoff \t    18,00
4- \t   Bife acebolado   15,00
5- \t   Pão com ovo\t    5,00
                       
Escolha o prato que deseja: """))
  
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

    soma += preco

    continuar = input("\nDeseja escolher outro prato? ")

    if continuar == "sim":
        break

print(f"\nTotal a pagar: R${soma}")
