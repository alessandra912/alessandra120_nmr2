import os
os.system ("clear")

primeiro_numero = float(input("Digitar o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

media = (primeiro_numero + segundo_numero) / 2

produto = primeiro_numero * segundo_numero

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print("\nExibindo resultados: ")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")