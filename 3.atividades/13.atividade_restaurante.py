import os
os.system ("clear")

# FAÇA UM ALGORITMO QUE MOSTRE UM MENU COM OPÇÕES DE UM CARDÁPIO DE RESTAURANTE
# PARA UMA PESSOA. 
# A PESSOA VAI ESCOLHER O PRATO DESEJADO DIGITANDO O CÓDIGO DO PRATO.
# APÓS ESCOLHER O PRATO, O ALGORITMO DEVE MOSTRAR O NOME E VALOR DO PRATO ESCOLHIDO. 

# ENTRADA
opção = int(input("""
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$ 25,00
2 \t Lasanha  \t\t R$ 20,00
3 \t Strogonoff \t\t R$ 18,00
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00                  
                                                                              
 Digite a opção desejada:                               
"""))

# PROCESSAMENTO
match opção:
    case 1:
        print ("picanha - 25,00")    
    case 2:
        print ("lasanha - 20,00")
    case 3:
        print ("strognoff - 18,00")
    case 4:
        print ("bife_acebolado - 15,00")
    case 5:
        print  ("pão_com_ovo - 5,00")

    case _: print ("Opção inválida.") 