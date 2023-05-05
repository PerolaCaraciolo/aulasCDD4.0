# Revisão 02:

# 1. Crie um algoritmo que leia um número diferente de zero e diga se este número é positivo ou negativo.
# 2. Colocar numa repetição.

sim = 1

while sim == 1:      # O professor ia iniciar a questão usando "WHILE = TRUE".
    num = int(input("Digite um número diferente de \"0\": "))
    if num != 0:
        if num < 0:
            print(f"O número {num} é negativo.")
        else:
            print(f"O número {num} é positivo.")
    else:
        print("NÚMERO INVÁLIDO!")

    sim = int(input("\n1 - Deseja repetir \n2 - Encerrar \n"))
