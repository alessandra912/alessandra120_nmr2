# Elabore um algoritmo para solicitar ao usuário o login e a senha.
# considere que os dados do usuário já estão cadastrados.
# caso o login e a senha estejam corretos, mostre a mensagem:
# "Bem-vindo!"
# caso contrario monstre
# "Senha ou usuario inválido"

import os
os.system ("clear")


login_cadastrado = "marta"
senha_cadastrada = "123"

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos!")    