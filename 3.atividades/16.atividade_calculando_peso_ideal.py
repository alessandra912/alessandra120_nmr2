import os
os.system ("clear")
# FAÇA UM PROGRAMA QUE CALCULE O "PESO IDEAL" DE UM USUÁRIO DE ACORDO COM UM 
# CARACTERE IDENTIFICADOR DE SEXO ("M" PARA MASCULINO OU "F" PARA FEMININO)
# INSERIDO PELO MESMO. A FÓRMULA PARA CADA UM DOS DOIS CASOS ESTÁ DEFINIDA ABAIXO.
# CASO "M", UTILIZE A FÓRMULA:
# (72.7 X ALTURA) - 58
# CASO "F", UTILLIZE A FÓRMULA:
# (62.1 X ALTURA) - 44.7

altura = float(input("Digite sua altura: "))
sexo = input ("Digite seu sexo: ")

match sexo:
    case "M"  | "m":
        peso_ideal = (72.7 * altura) - 58
        print(f"/nPeso ideal: {peso_ideal:.2f}")
    case "F" | "f":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"/nPeso ideal: {peso_ideal:.2f}")
    case _:
        print("Opção inválida")    
