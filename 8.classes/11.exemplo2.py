import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Paciente:
    # Atributos: são variáveis que pertecem a classe.
    nome:str
    idade:int

    # Método: é uma função que pertence a classe.
    # Este método para exibir dados do paciente.
    def exibindo_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n")

# Atibuindo dados ao paciente1.
paciente1 = Paciente(
                    nome= input("Digite seu nome: "), 
                    idade= int(input("Digite sua idade: ")))

# Exibindo dados do paciente.
print("\nExibindo os dados do usuário.")
paciente1.exibindo_dados()