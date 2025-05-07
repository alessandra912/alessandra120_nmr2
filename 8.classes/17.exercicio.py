import os
from dataclasses import dataclass
os.system("cls || clear")

lista_usuarios = []
QUANTIDADE_USUARIOS = 2

@dataclass
class informaçoes:
    nome:str
    data_nascimento:str
    rg:int
    cpf:int

    def exibir_detalhes(self): print(
            f"\nNome: {self.nome}\n"
            f"Data de Nascimento: {self.data_nascimento}\n"
            f"RG: {self.rg}\n"
            f"CPF: {self.cpf}\n")

print("=== Solicitando dados do usuário ===")
for i in range(QUANTIDADE_USUARIOS):
    usuarios = informaçoes(
        nome = input("\nDigite seu nome: "),
        data_nascimento = input("Digite sua data de nascimento: "),
        rg = int(input("Digite seu RG: ")),
        cpf = int(input("Digite seu CPF: ")))
    
    lista_usuarios.append(usuarios)

nome_arquivo = "Funcionário.txt"
with open(nome_arquivo, "a") as arquvivo_usuarios:
    for usuarios in lista_usuarios:
        arquvivo_usuarios.write(f"{usuarios.nome}, {usuarios.data_nascimento}, {usuarios.rg}, {usuarios.cpf}\n")

print("\n=== Dados salvo com sucesso ===")

try:
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readline()
        for linha in linhas:
            print(f"{linhas.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado.")