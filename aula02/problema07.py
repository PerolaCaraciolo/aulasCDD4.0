# Problema 07:

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: R$ "))
percentualAumento = float(input("Digite o percentual de aumento do seu salário: "))

aumento = (percentualAumento/100)*salario

novoSalario = salario + aumento

print(f"Após aumento, {nome} passou a receber um salário de R${novoSalario}.")
