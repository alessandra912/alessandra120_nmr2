import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informacoes:
    nome:str
    email:str
    telefone:int
    endereco:str

print("Solicitando dados: ")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = int(input("Digite seu telefone: "))
endereco = input("Digite seu endereço: ")
informacao = informacoes(nome, email, telefone, endereco)

print("\nExibindo informações: ")
print(f"Nome: {informacao.nome}\nE-mail: {informacao.email}\nTelefone: {informacao.telefone}\nEndereço: {informacao.endereco}" )