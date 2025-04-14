import os
os.system("cls || clear")
QUANTIDADE_NOTAS = 4

def situacao(media):
    if media >= 7:
        resultado = "Aprovado!"
    elif media >= 5:
        resultado = "Recuperação!"
    else:
        resultado = "Reprovado!"
        return resultado

lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADE_NOTAS

resultado = situacao(media)

print()
for nota in lista_notas: 
    print("Nota:", nota)

print("Média:", media)
print("Resultado:", resultado)