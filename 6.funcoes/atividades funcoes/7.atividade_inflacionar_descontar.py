import os
os.system("cls || clear")

def inflacionar_preco(preco):
    if preco < 100:
        resultado = preco * 1.10
        resultado = preco * 1.20
        return resultado
    
def descontar_preco(preco):
    if preco < 100:
        desconto = preco * 0.10
    else:
        desconto = preco * 0.20
        return desconto

produto = float(input("Digite o preço do produto: "))

preco_inflacionado = inflacionar_preco(produto)
preco_com_desconto = descontar_preco(produto)

print(f"Preço inflacionado: {preco_inflacionado}")
print(f"Preço com desconto: {preco_com_desconto}")