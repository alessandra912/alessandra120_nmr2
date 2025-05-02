import os
os.system("cls | clear")

contador = 0
continua = "s"

while True:   
    #comandos a serem repetidos
    print("repetindo...")
 
    continua = input("Tecle 's' se deseja continuar: ").strip().lower()
    contador += 1
  
    if continua != 's':
        break

if contador == 0:
    print("O bloco NÃO foi repetido.")
else:
    print(f"O bloco foi repetido {contador} vezes.")