import os
os.system("cls || clear")
QUANTIDADE_NOTAS = 4

lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = int(input("Digite uma nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADE_NOTAS 

if media >= 7:
        resultado = "Aprovado!"
elif media >= 5:
        resultado = "Recuperação!"
else:
    resultado = "Reprovado!"

media = sum(lista_notas) / QUANTIDADE_NOTAS 

print()
for nota in lista_notas: 
    print("Nota:", nota)

print("Média:", media)
print("Resultado:", resultado)