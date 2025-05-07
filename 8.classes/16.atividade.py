import os
from dataclasses import dataclass
os.system("cls || clear")

lista_de_livros = []
QUANTIDADE_DE_LIVROS = 1

@dataclass
class Autor:
    nome:str
    biografia:str

@dataclass
class Livro:
    titulo:str
    ano:int
    autor:Autor

    def exibir_detalhes(self): print(
            f"Título: {self.titulo}\n"
            f"Ano: {self.ano}\n"
            f"Autor: {self.autor.nome}\n")

for i in range(QUANTIDADE_DE_LIVROS):
    livros = Livro(
        titulo = input("Digite o título do livro: "),
        ano = int(input("Ano de publicação: ")),
        autores = Autor(
            nome = input("Digite o nome do autor: "),
            bibliografia = input("Informações sobre bibliográfia: ")))

    lista_de_livros.append(livros)

nome_arquivo = "Livros.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_livros:
    for livros in lista_de_livros:
        arquivo_livros.write(f"{livros.titulo}, {livros.ano}, {livros.autor.nome}\n")

livros.exibir_detalhes()