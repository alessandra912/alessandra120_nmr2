import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoa:
    nome:str
    idade:int

@dataclass
class Pet:
    nome:str
    idade:int
    raca:str

#Exemplo de uso de classe
pessoa1 = Pessoa("Marta", 30)
pessoa2 = Pessoa("José", 40)

pet1 = Pet("Toto", 4, "Pastor Alemão")
pet2 = Pet("Hulk", 6, "Pitbull")

print("Dados das pessoas: ")
print(f"Nome: {pessoa1.nome}, Idade:{pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade:{pessoa2.idade}")

print("\nDados dos pets: ")
print(f"Nome: {pet1.nome}, Idade:{pet1.idade}, Raça {pet1.raca}")
print(f"Nome: {pet2.raca}, Idade:{pet2.idade}")