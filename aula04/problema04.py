# Problema 04:

# Ler uma variável de número inteiro e mostrar a tabuada desse número.

num = int(input("Digite um número inteiro: "))

for tabuada in range(1, 11):     # Na tabuada, vou querer que apareça do múltiplo de "1" até o de "10", logo: (1, 11)
    print(f"{num} * {tabuada} = {num*tabuada}")





"""     ABAIXO É COMO EU TINHA FEITO, usando um contador externo pra poder ajudar na contagem.
            Ele disse que "eu tava roubando" fazendo assim. Pra usar o conceito mesmo do "FOR" é como está acima.
            
count = 1

for tab in range(10):
    print(f"{num} * {count} = {num*count}")
    count += 1
"""
