# Crie um programa que solicite ao usuário seu login e uma senha. 
# O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. 
# O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse 
# o número de tentativas, o programa deve ser finalizado.

import os

os.system("cls | clear")

login_cadastrado = "eu"
senha_cadastrada = "123"

for i in range(3):
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login_cadastrado == login  and senha_cadastrada == senha:
            print("Bem vindo!")
            break
        else: 
            print("Acesso negado.\n")
            if i == 2:
                print("Número de tentativas acima do permitido.")