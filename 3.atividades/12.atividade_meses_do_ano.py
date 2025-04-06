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
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")
