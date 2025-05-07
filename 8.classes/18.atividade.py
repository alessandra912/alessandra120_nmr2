import os
from dataclasses import dataclass
os.system("cls || clear") 

@dataclass
class funcionario:
    nome:str
    data_de_admissao:str
    matricula:int
    endereco:str

@dataclass
class cliente:
    nome:str
    data_nascimento:str
    endereco:str

lista_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 3
lista_clientes = []
QUANTIDADE_CLIENTES = 3

def exibir_dados(self):print(
            f"Nome {self.nome}\n",
            f"Data de Admissão {self.data_de_admissao}\n"
            f"Matricula {self.matricula}\n"
            f"Endereço {self.endereco}\n"
            f"Nome {self.nome}\n"
            f"Data de nascimento {self.data_de_nascimento}"
            f"Endereço {self.endereco}") 

print("== Funcionários ==")
for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionarios = funcionario(
        nome = input("\nDigite seu nome: "),
        data_de_admissao = input("Digite a data de admissão do funcionário: "),
        matricula = int(input("Digite a matricula: ")),
        endereco = input("Digite o endereço: "))
    lista_funcionarios.append(funcionarios)

print("\n== Clientes ==")  
for i in range(QUANTIDADE_CLIENTES):
    clientes = cliente(
        nome = input("\nDigite seu nome: "),
        data_nascimento = input("Digite a data de nascimento: "),
        endereco = input("Digite o endereço: "))
    lista_clientes.append(clientes)

print("\n=== Dados salvo com sucesso ====")
nome_arquivo = "Funcionários3.txt"
with open(nome_arquivo, "a") as arquivo_funcionarios:
    for funcionarios in lista_funcionarios:
        arquivo_funcionarios.write(f"{funcionarios.nome}, {funcionarios.data_de_admissao}, {funcionarios.matricula}, {funcionarios.endereco}\n")

nome_arquivo = "Clientes.txt"
with open(nome_arquivo, "a") as arquivo_clientes:
    for clientes in lista_clientes:
        arquivo_clientes.write(f"{clientes.nome}, {clientes.data_nascimento},{clientes.endereco}\n")

for funcionarios in lista_funcionarios:
    funcionarios.exibir_dados()
for clientes in lista_clientes:
    clientes.exibir_dados()