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
    nota = int(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADE_NOTAS

resultado = situacao(media)

print(f"\nMédia:", media)
print(f"Resultado:", resultado)