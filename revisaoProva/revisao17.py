# Revisão 17:

# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

qntd = int(input("Quantas maçãs? "))
valorDuzia = 1 * qntd
valorMenos = 1.3 * qntd

if qntd >= 12:
    print(f"A pagar por {qntd} maçãs: \nR${valorDuzia}")
else:
    print(f"A pagar por {qntd} maçã(s): \nR${valorMenos}")
