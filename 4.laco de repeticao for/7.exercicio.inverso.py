# Escrever um algoritmo que gera e escreve os números pares entre 100 e 120.

import os

os.system ("cls || clear")

print("NÚMEROS PARES")
for i in range (100, 121, 2):
    print(i)

print("FIM DO PROGRAMA") 

# Or

import os

os.system ("cls || clear")

print("NÚMEROS PARES")
for i in range (100, 121):
    if i % 2 == 0:
        print(i)

print("FIM DO PROGRAMA") 