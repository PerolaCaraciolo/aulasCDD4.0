# Problema 05:

# Receber um número do usuário e mostrar todos os números ímpares do intervalo de 1 até o número digitado.

num = int(input("Digite um número inteiro a partir de 1: "))

for impar in range(1, num+1):   # Pra utilizar do número digitado também, preciso somar "1" a ele no argumento do "FOR",
                                # se não ele não vai ser considerado, independente de ser um número mesmo ou variável.
    if impar % 2 != 0:     # Conceito pra imprimir só os números ímpares.
        print(f"{impar} é ímpar.")





"""     ABAIXO É COMO EU TINHA FEITO, já considerando que a partir de 1, se eu pulo de 2 em 2, só vão aparecer 
                números ímpares, mas ele disse que eu tava "roubando" de novo. Esqueci a palavra que ele usou, kkk, 
                mas ele falou que não mostra como realmente eu sei o conceito que prova ser par ou ímpar.
                
for imp in range(1, num, 2):
    print(imp)
"""
