# ESCREVA UM PROGRAMA UTILIZANDO O COMANDO MATCH-CASE QUE IMPRIMA UM
# MÊS DO ANO DE ACORDO COM O NÚMERO DIGITADO PELO USUÁRIO.
# EXEMPLO
# 1 - JANEIRO
# 2 - FEVEREIRO
# ...
# 12 - DEZEMBRO

mes = int(input("Digite o número para o mês do ano: "))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Número inválido!")
