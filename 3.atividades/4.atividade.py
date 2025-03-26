# Limpar o terminal.
import os
os.system ("clear")

# Elabore um algoritmo para solicitar dois números e ao final mostre
# na tela: 
# A média, a soma, o produto, o menor valor e o maior valor.
# Usando uma linha para cada resultado.

primeiro_numero = float(input("Digitar o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

# media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
media = soma / 2

produto = primeiro_numero * segundo_numero

if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else:
    menor = segundo_numero 
    maior = primeiro_numero

print("\nExibindo resultados: ")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")
