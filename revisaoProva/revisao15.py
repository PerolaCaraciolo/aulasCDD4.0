# Revisão 15:

# Escreva um algoritmo para ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem
# crescente.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))

if n1 > n2:
    print("Ordem crescente:\n", n2, n1)
else:
    print("Ordem crescente:\n", n1, n2)
