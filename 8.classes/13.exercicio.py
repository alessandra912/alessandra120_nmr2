import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informaçoes:
    nome:str
    idade:int
    peso:float
    altura:float
      
    def exibindo_dados(self):
        print(
             f"Nome: {self.nome}\n"
             f"Idade: {self.idade}\n"
             f"Peso: {self.peso}\n"
             f"Altura: {self.altura}\n")

lista_de_pessoas = []       
QUANTIDADE_PACIENTES = 2

for i in range(QUANTIDADE_PACIENTES):
    pessoas = informaçoes(
                nome = input("\nDigite seu nome: "),
                idade = int(input("Digite sua idade: ")),
                peso = float(input("Digite seu peso: ")),
                altura = float(input("Digite sua altura: ")))
    lista_de_pessoas.append(pessoas)

print("\nExibindo os dados do usuário.")
for pessoas in lista_de_pessoas:
    pessoas.exibindo_dados()