# Revisão 05:

# 1. Crie um algoritmo que leia um número e diga se ele é par ou ímpar.
# 2. Dizer se é positivo ou negativo.

num = int(input("Digite um número: "))

if num % 2 == 0:
    if num > 0:
        print(f"O número {num} é par e positivo.")
    else:
        print(f"O número {num} é par e negativo.")
else:
    if num > 0:
        print(f"O número {num} é ímpar e positivo.")
    else:
        print(f"O número {num} é ímpar e negativo.")
