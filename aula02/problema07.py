# Problema 07:

# (04) - Faça um programa para ler o nome de uma pessoa, a sua idade e o seu salário.
# (04) - Mostre essas informações na tela.

# Utilize da mesma questão 04 mas também receba o percentual de aumento do salário e imprima qual o novo
# salário desse funcionário.

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: R$ "))
percentualAumento = float(input("Digite o percentual de aumento do seu salário: "))

aumento = (percentualAumento/100)*salario

novoSalario = salario + aumento

print(f"Após aumento, {nome} passou a receber um salário de R${novoSalario}.")
