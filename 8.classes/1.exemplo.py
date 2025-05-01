import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoa:
    nome:str
    idade:int

#Exemplo de uso de classe
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

print(f"Nome: {pessoa1.nome}, Idade:{pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade:{pessoa2.idade}")