import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class endereco:
    logradouro:str
    numero:str
  
@dataclass
class pessoa:
    # Atributos da classe (Variáveis que pertence a uma classe).
    nome:str
    idade:int
    endereco:endereco # Classe endereço

    # Método da classe (função que pertence a uma classe).
    def exibindo_dados(self):
        print(f"Nome: {self.nome}, \
                Idade: {self.idade}, \
                Logradouro: {self.endereco.logradouro}, \
                Número: {self.endereco.numero}" )

endereco1 = endereco("Rua A", "33")
pessoa1 = pessoa("Marta", 22, endereco1)

print("Dados de pessoas: ")
pessoa1.exibindo_dados()
