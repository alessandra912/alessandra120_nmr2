import os
os.system("cls || clear")

def dividindo_e_potencializando(peso, altura):
      return peso / altura ** 2
      
def situacao(imc):
      if imc >= 40:
         Classificacao = "Obesidade grau 3"
         recomendacao =  "Busque assistência médica imediatamente"
      elif imc >= 25:
         classificacao = "Peso normal" 
         recomendacao = "Mantenha hábitos saudáveis!"
      elif imc >= 30:
         classificacao = "Sobrepeso" 
         recomendacao = "Considere uma dieta balanciada e atividade física."
      elif imc >= 35:
         classificacao = "Obesidade grau 2"  
         recomendacao = "Consulte um médico para avaliação e orientação."
      elif imc >= 39.9:
         classificacao = "Obesidade grau 2"  
         recomendacao = "Consulte um médico para avaliação e orientação."
      else:
         imc < 18.5
         Classificacao = "Abaixo do peso! "
         recomendacao =  "Consulte um nutricinista."
         return classificacao, recomendacao

peso = float(input("Digite seu peso em 'kg': "))
altura = float(input("Digite sua altura em 'm': "))

imc = dividindo_e_potencializando(peso, altura)

classificacao, recomendacao = situacao (imc)

print(f"Imc: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {recomendacao}")