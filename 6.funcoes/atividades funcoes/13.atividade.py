import os
os.system("cls || clear")

def dividindo_e_potencializando(peso, altura):
   return peso / altura ** 2

peso = float(input("Digite seu peso em 'kg': "))
altura = float(input("Digite sua altura em 'm': "))

imc = dividindo_e_potencializando(peso, altura)

print(f"Imc: {imc:.2f}")

match peso, altura:
      case 1:
         imc < 18.5
         print("Classificação: Abaixo do peso")
         print("Recomendação: Consulte um nutricinista.")
      case 2:
         imc == 18.5, 24.9
         print("Classificação: Peso normal")
         print("Recomendação: Mantenha hábitos saudáveis!")
      case 3:
         imc == 25, 29.9
         print("Classificação: Sobrepeso")
         print("Recomendação: Considere uma dieta balanciada e atividade física.")
      case 4:
         imc == 30, 34.9
         print("Classificação: Obesidade grau 1")
         print("Recomendação: Procure orientação de um profissional de saúde.")
      case 5:
         imc == 35, 39.9
         print("Classificação: Obesidade grau 2")
         print("Recomendação: Consulte um médico para avaliação e orientação.")
      case 6:
         imc > 40
         print("Classificação: Obesidade grau 3")
         print("Recomendação: Busque assistência médica imediatamente.")