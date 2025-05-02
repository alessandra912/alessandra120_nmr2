#Foi feita uma pesquisa entre os habitantes de uma região.  Foram coletados os dados de idade, 
# sexo (M/F) e salário. 
#Faça um algoritmo que informe:
#a) a média de salário do grupo;
#b) maior e menor idade do grupo;
#c) quantidade de mulheres com salário a partir de R$ 5.000,00.
#Crie um menu com três opções.
#Código |   Descrição
#1      |   Adicionar pessoa
#2      |   Exibir resultados
#3      |    Sair
#O final da leitura de dados se dará com quando o usuário digitar o número código 3. 
#Ao adicionar uma família, deve-se limpar o terminal e apresentar o menu novamente.


import os
import time
os.system("cls | clear")

contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 9999
mulheres5k = 0
media = 0

while True:
    print("""
========OPÇÕES=======
Código|  Descrição
1     | Adicionar pessoa
2     | Exibir resultados
3     | Sair
""")
    
    opcao = int(input("Digite a opção desejada: "))
    
    match opcao:
        case 1:
            idade = int(input("Digite sua idade: "))
            sexo = input("Informe seu sexo - Use 'M' ou 'F': ").upper()
            salario = float(input("Digite seu salário: "))
            contador += 1
            soma_salario += salario
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1
            os.system("cls | clear")
        case 2: 
            if contador > 0:
                media_salarial = soma_salario / contador
                print("\n= Exibindo resultados =")
                print(f"Média salarial do grupo: {media_salarial}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário a partir de 5k: {mulheres5k}")
            else: 
                print("\nNão foram informados os dados necessários.")
                time.sleep(3)
                os.system("cls | clear")
        case 3:
            print("\n=Fim =")
            break
        case _:
            print("\nOpcao inválida.")
            time.sleep(3)
            os.system("cls | clear")



    
