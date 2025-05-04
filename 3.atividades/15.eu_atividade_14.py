# Limpar terminal 
import os
os.system ("clear")


valor_do_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1 - A vista
2 - Parcelado                                                             
Digite a forma de pagamento: """))

match forma_de_pagamento:
    case 1:
        # Aplicando desconto de 10%.
        desconto = valor_do_produto * 0.10
        valor_pagar = valor_do_produto - desconto

        # Exibindo resultado.
        print(f"\nValor do produto: R$ {valor_do_produto}")
        print(f"Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto}")
        print(f"Total da pagar: R$ {valor_pagar}")
    case 2:
       quantidade_de_parcelas = int(input(
"""\n1 - 2 parcelas
2 - 3 parcelas
3 - 4 parcelas
4 - 5 parcelas
5 - 6 parcelas
selecione a quantidade de parcelas: """))
       if quantidade_de_parcelas >= 1 and quantidade_de_parcelas <= 6:
            valor_da_parcela = valor_do_produto / quantidade_de_parcelas

        # Exibindo resultado.
            print(f"\nValor do produto: R$ {valor_do_produto}")
            print(f"Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {quantidade_de_parcelas}")
            print(f"Total à prazo: R$ {valor_do_produto}")           
    case _:
        print("Opção inválida.")