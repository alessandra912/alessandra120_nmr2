# Limpar o terminal.
import os
os.system ("clear")

# Elabore um algoritmo para solicitar ao usuário três notas.
# Calcule a média do aluno.
# Caso a média seja menor que 7, o aluno será reprovado.
# Mostrar: média e se está aprovado ou reprovado.

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3 

print(f"Média: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("Aprovado!")    