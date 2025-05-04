import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Paciente:
    # Atributos: são variáveis que pertecem a classe.
    nome:str
    idade:int

    # Método: é uma função que pertence a classe.
    # Este método para exibir dados do paciente.
    def exibindo_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n")

# Criando uma lista.
lista_de_pacientes = []
QUANTIDADE_PACIENTES = 2

# Atibuindo dados ao paciente1.
for i in range(QUANTIDADE_PACIENTES):
    paciente = Paciente(
                    nome= input("\nDigite seu nome: "), 
                    idade= int(input("Digite sua idade: ")))
    lista_de_pacientes.append(paciente)
    print

# Salvando em um arquivo com .txt
nome_arquivo = "Dados_paciente.txt"
with open(nome_arquivo, "a") as arquivos_pacientes: # 'w' para acumular arquivos, or 'a' para apagar arquivo a cada novo arquivo acrescentado
    for paciente in lista_de_pacientes:
        arquivos_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")

print("\nDados salvos com sucesso.")

# Exibindo dados do paciente.
# print("\nExibindo os dados do usuário.")
# for paciente in lista_de_pacientes:
    # paciente.exibindo_dados()