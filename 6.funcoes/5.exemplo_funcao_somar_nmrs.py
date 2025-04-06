#faça uma função sem retorno com o nome: logo_senai()
#limpando o terminal e inserindo: === SENAI DENDEZEIROS ===

#solicite ao usuario dois números
#cada um em uma variável diferente
#crie uma função com retorno para somar os dois números informados pelo usuario.

import os

def logo_senai():
    os.system("cls || clear")
    print("=== SENAI DENDEZEIROS ===")

def somar(n1, n2):
    return n1 +n2

logo_senai()
n1 = int(input("Digite o primeiro número: "))

logo_senai()
n2 = int(input("Digite o segundo número: "))

soma = somar(n1, n2)

logo_senai()
print(f"Soma: {soma}")





