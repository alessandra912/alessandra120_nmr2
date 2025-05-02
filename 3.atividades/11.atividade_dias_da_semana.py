import os
os.system ("clear")

# DESENVOLVA UM PROGRAMA QUE RECEBA COMO ENTRADA UM NÚMERO INTEIRO QUE
# REPRESENTE UM DOS 7 DIAS DA SEMANA E IMPRIMA NA TELA SE ESSE DIA É ÚTIL
# FINAL DE SEMANA OU INVÁLIDO, 
# CONSIDERE QUE DOMINGO É DIA 1 E SÁBADO O DIA 7.

# ENTRADA
Dia = int(input("Digite um número para o dia da semana: "))

# PROCESSAMENTO
match Dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido!")
