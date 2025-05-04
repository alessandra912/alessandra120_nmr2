import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informaçoes:
    nome:str
    data_de_nascimento:str
    rg:str
    cpf:str

    def exibindo_dados(self):
            print(
             f"Nome: {self.nome}\n"
             f"Data de nascimeto: {self.data_de_nascimento}\n"
             f"RG: {self.rg}\n"
             f"CPF: {self.cpf}\n")

lista_usuarios = []
QUANTIDADE_USUARIOS = 5

for i in range(QUANTIDADE_USUARIOS):
    funcionarios = informaçoes(
                nome = input("\nDigite seu nome: "),
                data_de_nascimento = input("Digite sua Data de nascimento: "),
                rg = input("Digite seu RG: "),
                cpf = input("Digite seu CPF: "))
    lista_usuarios.append(funcionarios)

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivos_funcionarios:
    for funcionarios in lista_usuarios:
        arquivos_funcionarios.write(f"Nome: {funcionarios.nome}\nData de nascimeto: {funcionarios.data_de_nascimento}\nRG: {funcionarios.rg}\nCPF: {funcionarios.cpf}")

print("\nDados salvos com sucesso.")

print("\n====Exibindo os dados do usuário====")
for funcionarios in lista_usuarios:
    funcionarios.exibindo_dados()