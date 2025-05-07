import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class informaçoes:
    nome:str
    autor:str
    categoria:str
    preco:float

    def exibindo_dados(self):
            print(
             f"Nome: {self.nome}\n"
             f"Autor: {self.autor}\n"
             f"Categoria: {self.categoria}\n"
             f"Preco: {self.preco}\n")

lista_livros = []
QUANTIDADE_DE_LIVROS = 3

for i in range(QUANTIDADE_DE_LIVROS):
    livraria = informaçoes(
                nome = input("\nDigite o nome do livro: "),
                autor = input("Digite o autor: "),
                categoria = input("Digite a categoria: "),
                preco = float(input("Digite o preço: ")))
    lista_livros.append(livraria)

nome_arquivo = "catalogo_livros.txt"
with open(nome_arquivo, "a") as arquivos_livraria:
    for livraria in lista_livros:
        arquivos_livraria.write(f"{livraria.nome}\n, {livraria.autor}\nCategoria: {livraria.categoria}\nPreço: {livraria.preco}")

print("\nDados salvos com sucesso.")

print("\nExibindo os dados do usuário.")
for livraria in lista_livros:
    livraria.exibindo_dados()