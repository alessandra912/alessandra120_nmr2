import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informacoes:
    nome:str
    idade:int
    peso:float
    altura:float

informacao = informacoes("Alessandra", 21, 75, 1.65)

print("\nExibindo informações: ")
print(f"Nome: {informacao.nome}, Idade: {informacao.idade}, Peso: {informacao.peso}, Altura: {informacao.altura}" )


