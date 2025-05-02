import os
os.system ("clear")
# Entrada
matricula = int(input("Digite sua matrícula: "))
ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
tempo_de_trabalho = int(input("Digite seu tempo de trabalho em anos: "))

# Processamento
idade = 2025 - ano_de_nascimento

if idade >= 65 or tempo_de_trabalho >= 30:
    resultado = "Requer aponsetadoria."
else:
    resultado = "Não requer aposentadoria"

# Saída
print(f"\nMatrícula: {matricula}")
print(f"Idade: {idade} anos")
print(f"Tempo de trabalho: {tempo_de_trabalho} anos")
print(f"Resultado: {resultado}")