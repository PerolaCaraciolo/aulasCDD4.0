# Problema 09:

# Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive).
# Considere que o N será sempre maior que ZERO.

num = int(input("Digite um valor inteiro e maior que 1: "))

for valor in range(1, num+1):
    print(valor)
