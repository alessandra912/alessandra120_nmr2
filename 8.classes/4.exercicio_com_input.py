import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informacoes:
    nome:str
    idade:int
    peso:float
    altura:float

print("Solicitando dados: ")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

informacao = informacoes(nome=nome, idade=idade, peso=peso, altura=altura)
informacao = informacoes(nome, idade, peso, altura)

print("\nExibindo informações: ")
print(f"Nome: {informacao.nome}, Idade: {informacao.idade}, Peso: {informacao.peso}, Altura: {informacao.altura}" )
print(f"Nome: {informacao.nome}, Idade: {informacao.idade}, Peso: {informacao.peso}, Altura: {informacao.altura}" )
