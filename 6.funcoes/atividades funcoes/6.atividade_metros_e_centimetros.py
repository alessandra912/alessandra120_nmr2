import os
os.system("cls || clear")

def converter_centimetros(centimetros):
    return centimetros * 100

metros = float(input("Digite um valor em metros: "))

centimetros = converter_centimetros(metros)

print(f"{metros} metros é igual a {centimetros} centímetros. ")