import os

os.system ("clear")

# Elabore um algoritmo para solicitar ao usuário um valor e
# Escrever a mensagem: "É MAIOR QUE 10!".
# Se o valor lido for maior que 10, caso contrário
# Escrever "NÃO É MAIOR QUE 10!"
# Verifique se o número digitado é igual a 10, caso seja,
# Escreva a mensagem: "O número é igual a 10!" 

valor = int(input("Digite o valor: "))

if valor == 10:
   print("É IGUAL A 10!")
elif valor > 10:
    print("É MAIOR QUE 10!")   
else: 
    print("NÃO É MAIOR QUE 10!")