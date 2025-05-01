import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informacoes:
    nome:str
    email:str
    telefone:int
    endereco:str

    def exibindo_dados(self):
        print("\nExibindo informações: ")
        print(f"Nome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}" )

print("Solicitando dados: ")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = int(input("Digite seu telefone: "))
endereco = input("Digite seu endereço: ")

informacao = informacoes(nome, email, telefone, endereco)
informacao.exibindo_dados()
