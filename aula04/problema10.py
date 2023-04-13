# Problema 10:

# Modifique o exercício anterior para aceitar somente valores maiores que 0 para N. Caso o valor
# informado (para N) não seja maior que 0, deverá ser lido um novo valor para N.

num = int(input("Digite um número maior que 0: "))
if num <= 0:
    num = int(input("VALOR INVÁLIDO! \nDigite um número maior que 0: "))
    for valor in range(1, num+1):
        print(valor)
else:
    for valor in range(1, num+1):
        print(valor)
