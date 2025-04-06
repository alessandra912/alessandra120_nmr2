import os
os.system ("clear")

nome = input("Digite o nome do aluno: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

print(f"Média: {media}")

if media >= 9:
    conceito = "A"
elif media > 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

match conceito:
    case "A" | "B" | "C":
        print("Aprovado!")
    case "D" | "E":
        print("Reprovado!")
    case _:
        print("opção inválida!")