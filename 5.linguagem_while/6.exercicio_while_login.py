# Crie um programa que solicite ao usuário seu login e uma senha. 
# O programa deve continuar pedindo o login e a senha
# até que ambos estejam corretos.

import os

os.system("cls | clear")

login_cadastrado = "eu"
senha_cadastrada = "123"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login_cadastrado == login and senha_cadastrada == senha:
        print("Bem vindo!.\n")
        break
    else:
        print("Acesso negado!")