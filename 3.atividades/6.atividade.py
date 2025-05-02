import os
os.system ("clear")

# Elaboare um algoritmo usando operações lógicas para
# solicitar ao usuário 2 números e escrever:
# Os dois números informados
# O maior número
# O menor número

primeiro_numero = float(input("Digite primeiro número: "))
segundo_numero = float(input("Digite o segundo numero: "))

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print()
print(f"Primeiro_número {primeiro_numero}")
print(f"Segundo_número {segundo_numero}")
print(f"Maior_número: {maior}")
print(f"Menor_número: {menor}")

# if primeiro_numero == segundo_numero:
#    print("Os números são iguais.")
# else:
#    print(f"Maior número: {maior}")
#    print(f"Menor número: {menor}")