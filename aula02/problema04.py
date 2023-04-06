# Problema 04:

# Faça um programa para ler o nome de uma pessoa, a sua idade e o seu salário.
# Mostre essas informações na tela.

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
salario = float(input("Digite seu salário: R$ "))    # Poderia não colocar o "FLOAT" tbm pq não vou usá-lo em contas.

print(f"{nome}, {idade} anos, possui salário de R${salario}.")
