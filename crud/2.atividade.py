import os
import time
from dataclasses import dataclass
os.system ("cls || clear")

@dataclass
class informações:
    nome:str
    data_nascimento:str
    cpf:str
    funcao:str

lista_de_informações = []

def verificar_lista_vazia(lista_de_informacoes):
    if not lista_de_informacoes:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar_informacoes(lista_de_informacoes):
        nome = input("\nInforme seu nome: ")
        lista_de_informacoes.append(nome)
        data_nascimento = input("Informe sua data de nascimento: ")
        lista_de_informacoes.append(data_nascimento)
        cpf = input("Digite seu CPF: ")
        lista_de_informacoes.append(cpf)
        funcao = input("Informe sua função: ")
        lista_de_informacoes.append(funcao)
        print(f"\n{nome}\n{data_nascimento}\n{cpf}\n{funcao} dados adicionados com sucesso.")

def visualizar_informacoes(lista_de_informacoes):
    if verificar_lista_vazia(lista_de_informacoes):
        return
    print("\n== Lista de informações ==")
    for nome in lista_de_informacoes:
        print(f"Nome - {nome}")
    for data_nascimeto in lista_de_informacoes:
        print(f"Data de nascimento - {data_nascimeto}")
    for cpf in lista_de_informacoes:
        print(f"CPF - {cpf}")
    for funcao in lista_de_informacoes:
        print(f"Função - {funcao}")

def atualizar_informacoes(lista_de_informacoes):
    if verificar_lista_vazia(lista_de_informacoes):
        return
    
    visualizar_informacoes(lista_de_informacoes)
    informacoes_antigas = input("Digite os dados do usuário que deseja atualizar: ")
    if informacoes_antigas in lista_de_informacoes:
        novas_informacoes = input(f"Digite as novos dados para {informacoes_antigas}: ")
        atualizacao = lista_de_informacoes.index(informacoes_antigas)
        lista_de_informacoes[atualizacao] = novas_informacoes
    else:
        print(f"\nOs dados {informacoes_antigas} não foram encontrados.")

def excluir_informacoes(lista_de_informacoes):
    if verificar_lista_vazia(lista_de_informacoes):
        return
    visualizar_informacoes(lista_de_informacoes)

    remover_informacoes = input("Digite os dados que deseja remover: ")
    if remover_informacoes in lista_de_informacoes:
        lista_de_informacoes.remove(remover_informacoes)
        print(f"{remover_informacoes} foram removidos com sucesso.")
    else:
        print(f"As informações {remover_informacoes} não foi encontrado.")

dados = []

while True:
    print("""
== Informações de funcionários ==
1- Adicionar
2- Vizualizar informações
3- Atualizar dados
4- Remover dados
5- Sair """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_informacoes(dados)
        case 2:
            visualizar_informacoes(dados)
            time.sleep(20)
        case 3:
            atualizar_informacoes(dados)
        case 4:
            excluir_informacoes(dados)
        case 5:
            print("\nEncerrando programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
            time.sleep(5)
    os.system("cls || clear") 