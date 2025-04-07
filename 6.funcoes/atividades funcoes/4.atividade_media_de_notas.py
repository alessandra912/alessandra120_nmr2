import os
os.system("cls || clear")

def calcular_media(nota_1, nota_2):
    soma = 0
    soma = nota_1 + nota_2
    resultado = soma / 2
    return resultado
def verificar_resultado(media):
    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")

print("= MEDIA DAS NOTAS =")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota_1, nota_2)
verificar_resultado(media)
