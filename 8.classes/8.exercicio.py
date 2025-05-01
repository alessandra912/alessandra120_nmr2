import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informacoes:
    logradouro:str
    numero:str
    cidade:str

@dataclass
class pessoa:
    nome:str
    email:str
    endereco:informacoes 

    def exibindo_dados(self):
        print(f"Nome: {self.nome}\n"
              f"E-mail: {self.email}\n"
              f"Logradouro: {self.endereco.logradouro}\n"
              f"Número: {self.endereco.numero}\n"
              f"Cidade: {self.endereco.cidade}")

print("Solicitando dados: ")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
endereco = input("Digite seu endereço: ")
logradouro = input("Digite seu largadouro: ")
numero = input("Digite o número do seu endereço: ")
cidade = input("Digite sua cidade: ")

endereco2 = informacoes(logradouro, numero, cidade)
informacao = pessoa(nome, email, endereco2)

print("\nExibindo informações: ")
informacao.exibindo_dados()