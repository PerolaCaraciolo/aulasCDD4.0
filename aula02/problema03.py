# Problema 03:

# Faça um programa para calcular a média de 2 notas e mostrar essa média e o nome do aluno.

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2

print(f"{nome}, sua média foi {media}.")
